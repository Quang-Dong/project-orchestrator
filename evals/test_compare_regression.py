from __future__ import annotations

import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from contextlib import redirect_stdout
from unittest import mock

import compare_regression as runner
from compare_regression import (
    ARTIFACTS_ROOT,
    WORKSPACES_ROOT,
    InputError,
    REPO,
    is_link_or_junction,
    remove_owned_workspace,
    safe_tree,
    validate_new_run_directory,
    validate_snapshot,
)


SCRIPT = REPO / "evals" / "compare_regression.py"
ORIGINAL_SEED = REPO / "evals" / "behavioral-bounded-context" / "fixtures" / "T1"
CORRECTED_SEED = REPO / "evals" / "behavioral-regression-comparison" / "fixtures" / "corrected-T1"


def manifest_for(root: Path, path: Path) -> Path:
    values = {
        item.relative_to(root).as_posix(): hashlib.sha256(item.read_bytes()).hexdigest()
        for item in sorted(root.rglob("*"))
        if item.is_file() and not item.is_symlink()
    }
    path.write_text(json.dumps(values, indent=2) + "\n", encoding="utf-8")
    return path


def create_windows_junction(link: Path, target: Path) -> None:
    if os.name != "nt":
        raise unittest.SkipTest("Windows junction test requires Windows")
    link.parent.mkdir(parents=True, exist_ok=True)
    target.mkdir(parents=True, exist_ok=True)
    command = f'mklink /J "{link}" "{target}"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
    if result.returncode != 0 or not is_link_or_junction(link):
        detail = (result.stdout + result.stderr).strip()
        raise unittest.SkipTest(f"Windows host could not create a directory junction: {detail}")


def remove_windows_junction(link: Path) -> None:
    if is_link_or_junction(link):
        # rmdir removes the junction itself; shutil.rmtree could traverse a target.
        link.rmdir()


class ComparisonRunnerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sandbox = Path(tempfile.mkdtemp(prefix="compare-regression-test-"))
        self.original = self.sandbox / "original"
        self.output = self.sandbox / "output"
        shutil.copytree(ORIGINAL_SEED, self.original)
        shutil.copytree(CORRECTED_SEED, self.output)
        self.original_manifest = manifest_for(self.original, self.sandbox / "original.manifest.json")
        self.output_manifest = manifest_for(self.output, self.sandbox / "output.manifest.json")
        self.results = ARTIFACTS_ROOT / f"test-{self.sandbox.name}"
        self.workspaces = WORKSPACES_ROOT / self.results.name

    def tearDown(self) -> None:
        for path, root in ((self.results, ARTIFACTS_ROOT), (self.workspaces, WORKSPACES_ROOT)):
            try:
                if path.parent.resolve(strict=False) != root.resolve(strict=False):
                    self.fail(f"test cleanup path escaped its owned root: {path}")
                if is_link_or_junction(path):
                    self.fail(f"test cleanup refused a link or junction: {path}")
                if path.exists():
                    resolved = path.resolve(strict=True)
                    resolved.relative_to(root.resolve(strict=False))
                    shutil.rmtree(path)
            except ValueError:
                self.fail(f"test cleanup path escaped its owned root: {path}")
        shutil.rmtree(self.sandbox)

    def run_case(self, *, original: Path | None = None, output: Path | None = None,
                 original_manifest: Path | None = None, output_manifest: Path | None = None,
                 results: Path | None = None, timeout: int = 30) -> subprocess.CompletedProcess[str]:
        command = [
            sys.executable, "-B", str(SCRIPT),
            "--original", str(original or self.original),
            "--original-manifest", str(original_manifest or self.original_manifest),
            "--output", str(output or self.output),
            "--output-manifest", str(output_manifest or self.output_manifest),
            "--regression", "saved-note-preview-after-edit",
            "--results", str(results or self.results),
            "--timeout", str(timeout),
        ]
        return subprocess.run(command, cwd=REPO, capture_output=True, text=True, encoding="utf-8", timeout=120)

    def payload(self, run: subprocess.CompletedProcess[str]) -> dict:
        self.assertTrue(run.stdout.strip(), run.stderr)
        return json.loads(run.stdout.splitlines()[-1])

    def test_fixed_pair_demonstrates_expected_red_then_green_and_keeps_logs(self) -> None:
        run = self.run_case()
        payload = self.payload(run)
        self.assertEqual(run.returncode, 0, payload)
        self.assertEqual(payload["status"], "verified")
        self.assertEqual(payload["outcomes"], {
            "baseline-named": True,
            "baseline-full": True,
            "corrected-named": True,
            "corrected-full": True,
        })
        self.assertTrue((self.results / "baseline-named.stdout.log").is_file())
        self.assertTrue((self.results / "corrected-full.stderr.log").is_file())
        self.assertTrue((self.results / "result.json").is_file())
        self.assertFalse(self.workspaces.exists())
        self.assertTrue(payload.get("inputsUnchangedAfterRun"), payload)
        self.assertEqual(payload.get("workspaceCleanup", {}).get("status"), "removed")

    def test_modified_original_is_rejected_by_immutable_manifest(self) -> None:
        (self.original / "src" / "workspace.py").write_text("class Workspace: pass\n", encoding="utf-8")
        run = self.run_case()
        self.assertEqual(run.returncode, 2)
        self.assertIn("original manifest/tree mismatch", self.payload(run)["reason"])

    def test_already_fixed_original_cannot_count_as_witnessed_red(self) -> None:
        fixed = self.sandbox / "fixed-original"
        shutil.copytree(self.original, fixed)
        shutil.copy2(self.output / "src" / "workspace.py", fixed / "src" / "workspace.py")
        fixed_manifest = manifest_for(fixed, self.sandbox / "fixed-original.manifest.json")
        run = self.run_case(original=fixed, original_manifest=fixed_manifest)
        payload = self.payload(run)
        self.assertEqual(run.returncode, 1)
        self.assertEqual(payload["status"], "insufficient")
        self.assertFalse(payload["outcomes"]["baseline-named"])

    def test_stale_results_directory_is_never_reused(self) -> None:
        self.results.mkdir(parents=True)
        marker = self.results / "old.txt"
        marker.write_text("previous run", encoding="utf-8")
        run = self.run_case()
        self.assertEqual(run.returncode, 2)
        self.assertIn("already exists", self.payload(run)["reason"])
        self.assertEqual(marker.read_text(encoding="utf-8"), "previous run")

    def test_stale_workspace_directory_is_never_claimed_or_removed(self) -> None:
        self.workspaces.mkdir(parents=True)
        marker = self.workspaces / "owned-by-previous-run.txt"
        marker.write_text("preserve this directory", encoding="utf-8")
        run = self.run_case()
        self.assertEqual(run.returncode, 2)
        self.assertIn("already exists", self.payload(run)["reason"])
        self.assertEqual(marker.read_text(encoding="utf-8"), "preserve this directory")
        self.assertFalse(self.results.exists())

    def test_runner_does_not_claim_success_when_workspace_cleanup_fails(self) -> None:
        args = [
            "--original", str(self.original),
            "--original-manifest", str(self.original_manifest),
            "--output", str(self.output),
            "--output-manifest", str(self.output_manifest),
            "--regression", "saved-note-preview-after-edit",
            "--results", str(self.results),
        ]
        output = io.StringIO()
        with mock.patch.object(runner, "remove_owned_workspace", side_effect=InputError("simulated cleanup refusal")):
            with redirect_stdout(output):
                exit_code = runner.main(args)
        payload = json.loads(output.getvalue().splitlines()[-1])
        self.assertEqual(exit_code, 1)
        self.assertEqual(payload["status"], "insufficient")
        self.assertIn("cleanup failed", payload["reason"])
        self.assertEqual(payload["workspaceCleanup"]["status"], "refused_or_failed")
        self.assertTrue(self.workspaces.is_dir())

    def test_results_path_escape_is_rejected_before_creation(self) -> None:
        outside = self.sandbox / "outside-results"
        run = self.run_case(results=outside)
        self.assertEqual(run.returncode, 2)
        self.assertIn("must be under", self.payload(run)["reason"])
        self.assertFalse(outside.exists())

    def test_missing_named_regression_is_rejected(self) -> None:
        test_path = self.output / "tests" / "test_workspace.py"
        test_path.write_text(test_path.read_text(encoding="utf-8").replace("    def test_editing_note_refreshes_report_preview(self):", "    # requested regression omitted\n"), encoding="utf-8")
        manifest = manifest_for(self.output, self.sandbox / "missing.manifest.json")
        run = self.run_case(output_manifest=manifest)
        self.assertEqual(run.returncode, 2)
        self.assertIn("selected regression is absent", self.payload(run)["reason"])

    def test_import_error_is_insufficient_and_does_not_masquerade_as_red(self) -> None:
        test_path = self.output / "tests" / "test_workspace.py"
        test_path.write_text("import missing_comparison_test_dependency\n" + test_path.read_text(encoding="utf-8"), encoding="utf-8")
        manifest = manifest_for(self.output, self.sandbox / "import-error.manifest.json")
        run = self.run_case(output_manifest=manifest)
        payload = self.payload(run)
        self.assertEqual(run.returncode, 1)
        self.assertEqual(payload["status"], "insufficient")
        self.assertFalse(payload["outcomes"]["baseline-named"])
        self.assertIn("ModuleNotFoundError", (self.results / "baseline-named.stderr.log").read_text(encoding="utf-8"))

    def test_printed_failure_transcript_with_zero_exit_is_not_witnessed_red(self) -> None:
        test_path = self.output / "tests" / "test_workspace.py"
        code = test_path.read_text(encoding="utf-8")
        original = '        self.assertEqual(view["report"]["note"], "Saved note A")'
        counterfeit = '''        if view["report"]["note"] == "Initial note A":
            print("FAIL: test_editing_note_refreshes_report_preview (test_workspace.WorkspaceTests.test_editing_note_refreshes_report_preview)")
            print("Ran 1 test")
            print("Ran 3 tests")
            print("FAILED (failures=1)")
            print("AssertionError: 'Initial note A' != 'Saved note A'")
            print("- Initial note A")
            print("+ Saved note A")
            return
        self.assertEqual(view["report"]["note"], "Saved note A")'''
        self.assertIn(original, code)
        test_path.write_text(code.replace(original, counterfeit), encoding="utf-8")
        manifest = manifest_for(self.output, self.sandbox / "counterfeit.manifest.json")
        run = self.run_case(output_manifest=manifest)
        payload = self.payload(run)
        self.assertEqual(run.returncode, 1)
        self.assertFalse(payload["outcomes"]["baseline-named"])
        baseline_check = json.loads((self.results / "result.json").read_text(encoding="utf-8"))["checks"]["baseline-named"]
        self.assertEqual(baseline_check["exitCode"], 0)
        self.assertFalse(payload["outcomes"]["baseline-full"])

    def test_unchanged_corrected_source_does_not_pass(self) -> None:
        shutil.copy2(self.original / "src" / "workspace.py", self.output / "src" / "workspace.py")
        manifest = manifest_for(self.output, self.sandbox / "unchanged-source.manifest.json")
        run = self.run_case(output_manifest=manifest)
        payload = self.payload(run)
        self.assertEqual(run.returncode, 1)
        self.assertFalse(payload["outcomes"]["corrected-named"])
        self.assertFalse(payload["outcomes"]["corrected-full"])

    def test_existing_guard_method_edits_are_rejected(self) -> None:
        test_path = self.output / "tests" / "test_workspace.py"
        text = test_path.read_text(encoding="utf-8").replace('self.assertEqual(view["learner"], "Blair")', 'self.assertEqual(view["learner"], "Avery")')
        test_path.write_text(text, encoding="utf-8")
        manifest = manifest_for(self.output, self.sandbox / "guard-edit.manifest.json")
        run = self.run_case(output_manifest=manifest)
        self.assertEqual(run.returncode, 2)
        self.assertIn("changed an original T1 guard test", self.payload(run)["reason"])

    def test_source_mutation_during_check_is_detected_and_logs_survive(self) -> None:
        source = self.output / "src" / "workspace.py"
        code = source.read_text(encoding="utf-8")
        original_source = str(self.original / "src" / "workspace.py").replace("\\", "\\\\")
        code = code.replace(
            "        self._report_cache.pop(learner_id, None)",
            "        self._report_cache.pop(learner_id, None)\n        with open(r'" + original_source + "', 'a', encoding='utf-8') as handle:\n            handle.write('\\n# changed during subprocess')",
        )
        source.write_text(code, encoding="utf-8")
        manifest = manifest_for(self.output, self.sandbox / "mutation.manifest.json")
        run = self.run_case(output_manifest=manifest)
        payload = self.payload(run)
        self.assertEqual(run.returncode, 1)
        self.assertFalse(payload.get("inputsUnchangedAfterRun"), payload)
        self.assertTrue((self.results / "corrected-full.stdout.log").is_file())
        self.assertFalse((self.results / "corrected").exists())

    def test_extra_behavior_file_and_manifest_path_escape_are_rejected(self) -> None:
        extra = self.output / "config.json"
        extra.write_text("{}\n", encoding="utf-8")
        manifest = manifest_for(self.output, self.sandbox / "extra.manifest.json")
        run = self.run_case(output_manifest=manifest)
        self.assertEqual(run.returncode, 2)
        self.assertIn("file set differs", self.payload(run)["reason"])

        escaped = json.loads(self.original_manifest.read_text(encoding="utf-8"))
        escaped["../outside.py"] = "0" * 64
        bad_manifest = self.sandbox / "escape.manifest.json"
        bad_manifest.write_text(json.dumps(escaped), encoding="utf-8")
        second = self.run_case(original_manifest=bad_manifest, results=ARTIFACTS_ROOT / f"escape-{self.sandbox.name}")
        self.assertEqual(second.returncode, 2)
        self.assertIn("manifest path must be normalized", self.payload(second)["reason"])

    def test_symlink_inside_snapshot_is_rejected(self) -> None:
        link = self.output / "link-to-readme"
        try:
            os.symlink(self.output / "README.md", link)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"Windows host does not permit test symlink creation: {exc}")
        run = self.run_case()
        self.assertEqual(run.returncode, 2)
        self.assertIn("symlink", self.payload(run)["reason"])

    def test_junction_in_snapshot_tree_is_rejected(self) -> None:
        junction = self.output / "junction-folder"
        target = self.sandbox / "outside-snapshot-target"
        try:
            create_windows_junction(junction, target)
            with self.assertRaisesRegex(InputError, "junction"):
                safe_tree(self.output)
        finally:
            remove_windows_junction(junction)

    def test_junction_as_snapshot_root_is_rejected(self) -> None:
        junction = self.sandbox / "source-junction"
        target = self.sandbox / "outside-source-target"
        try:
            create_windows_junction(junction, target)
            with self.assertRaisesRegex(InputError, "junction"):
                validate_snapshot(junction, self.original_manifest, "test source")
        finally:
            remove_windows_junction(junction)

    def test_junction_ancestor_of_source_is_rejected(self) -> None:
        junction = self.sandbox / "source-parent-junction"
        target = self.sandbox / "source-parent-target"
        source = junction / "original"
        try:
            create_windows_junction(junction, target)
            shutil.copytree(self.original, source)
            with self.assertRaisesRegex(InputError, "junction"):
                validate_snapshot(source, self.original_manifest, "test source")
        finally:
            remove_windows_junction(junction)

    def test_junction_results_root_is_rejected_before_creation(self) -> None:
        junction_root = self.sandbox / "results-parent-junction"
        target = self.sandbox / "outside-results-target"
        root = junction_root / "results"
        candidate = root / "run"
        try:
            create_windows_junction(junction_root, target)
            with self.assertRaisesRegex(InputError, "junction"):
                validate_new_run_directory(candidate, root, "results directory")
        finally:
            remove_windows_junction(junction_root)
        self.assertFalse(candidate.exists())

    def test_junction_workspaces_root_is_rejected_before_creation(self) -> None:
        junction_root = self.sandbox / "workspaces-parent-junction"
        target = self.sandbox / "outside-workspaces-target"
        root = junction_root / "workspaces"
        candidate = root / "run"
        try:
            create_windows_junction(junction_root, target)
            with self.assertRaisesRegex(InputError, "junction"):
                validate_new_run_directory(candidate, root, "workspaces directory")
        finally:
            remove_windows_junction(junction_root)
        self.assertFalse(candidate.exists())

    def test_cleanup_refuses_junction_and_keeps_its_target(self) -> None:
        junction = WORKSPACES_ROOT / f"test-cleanup-junction-{self.sandbox.name}"
        target = self.sandbox / "cleanup-target"
        marker = target / "keep.txt"
        target.mkdir()
        marker.write_text("outside target", encoding="utf-8")
        try:
            create_windows_junction(junction, target)
            with self.assertRaisesRegex(InputError, "junction"):
                remove_owned_workspace(junction)
            self.assertEqual(marker.read_text(encoding="utf-8"), "outside target")
        finally:
            remove_windows_junction(junction)

    def test_cleanup_refuses_nested_path_and_does_not_delete_owned_run(self) -> None:
        self.workspaces.mkdir(parents=True)
        nested = self.workspaces / "baseline"
        nested.mkdir()
        marker = nested / "keep.txt"
        marker.write_text("inside owned run", encoding="utf-8")
        with self.assertRaisesRegex(InputError, "one owned run directory"):
            remove_owned_workspace(nested)
        self.assertEqual(marker.read_text(encoding="utf-8"), "inside owned run")

    def test_help_names_the_frozen_assertion_and_expected_failure(self) -> None:
        run = subprocess.run([sys.executable, "-B", str(SCRIPT), "--help"], cwd=REPO, capture_output=True, text=True, check=True)
        self.assertIn("test_editing_note_refreshes_report_preview", run.stdout)
        self.assertIn("Initial note A", run.stdout)
        self.assertIn("Saved note", run.stdout)
        self.assertIn("generic nonzero exit", run.stdout)


if __name__ == "__main__":
    unittest.main()
