#!/usr/bin/env python3
"""Compare one frozen regression against original and corrected T1 source."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
DATA_ROOT = REPO / ".data"
ARTIFACTS_ROOT = DATA_ROOT / "artifacts" / "regression-comparison"
WORKSPACES_ROOT = DATA_ROOT / "workspaces" / "regression-comparison"
SOURCE_PATH = "src/workspace.py"
TEST_PATH = "tests/test_workspace.py"
REGRESSIONS = {
    "saved-note-preview-after-edit": {
        "test_file": TEST_PATH,
        "test_id": "test_workspace.WorkspaceTests.test_editing_note_refreshes_report_preview",
        "method": "test_editing_note_refreshes_report_preview",
        "expected_old": "Initial note A",
        "expected_new": "Saved note A",
    }
}
ORIGINAL_GUARD_METHODS = (
    "test_selection_updates_editor_and_report_for_each_learner",
    "test_reopening_a_preview_without_source_changes_is_stable",
)
EXIT_VERIFIED = 0
EXIT_INSUFFICIENT = 1
EXIT_INVALID = 2


class InputError(Exception):
    pass


def is_link_or_junction(path: Path) -> bool:
    """Detect symlinks, Windows junctions, and other Windows reparse points."""
    try:
        if path.is_symlink():
            return True
        is_junction = getattr(path, "is_junction", None)
        if callable(is_junction) and is_junction():
            return True
        if os.name == "nt":
            attributes = path.lstat().st_file_attributes
            reparse_point = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
            if reparse_point and attributes & reparse_point:
                return True
    except FileNotFoundError:
        return False
    return False


def reject_linked_path_components(path: Path, label: str) -> Path:
    """Return an absolute path only when no component is a link or reparse point."""
    absolute = Path(os.path.abspath(path))
    current = Path(absolute.anchor)
    if is_link_or_junction(current):
        raise InputError(f"{label} path contains a symlink, junction, or reparse point: {current}")
    for part in absolute.parts[1:]:
        current = current / part
        if is_link_or_junction(current):
            raise InputError(f"{label} path contains a symlink, junction, or reparse point: {current}")
    return absolute


def validate_new_run_directory(path: Path, root: Path, label: str) -> Path:
    """Require one fresh run directory directly beneath its repository-owned root."""
    root_abs = reject_linked_path_components(root, f"{label} root")
    path_abs = reject_linked_path_components(path, label)
    try:
        relative = path_abs.relative_to(root_abs)
    except ValueError as exc:
        raise InputError(f"{label} must be under {root_abs}") from exc
    if len(relative.parts) != 1:
        raise InputError(f"{label} must be a direct child of {root_abs}")
    run_id = relative.parts[0]
    if (not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,79}", run_id)
            or run_id.endswith((".", " "))
            or run_id.upper() in {"CON", "PRN", "AUX", "NUL", *(f"COM{i}" for i in range(1, 10)), *(f"LPT{i}" for i in range(1, 10))}):
        raise InputError(f"{label} has an invalid run ID: {run_id!r}")
    if path_abs.exists():
        raise InputError(f"{label} directory already exists; refusing stale or reused output: {path_abs}")
    try:
        resolved_root = root_abs.resolve(strict=False)
        resolved_parent = path_abs.parent.resolve(strict=False)
    except OSError as exc:
        raise InputError(f"cannot resolve {label} path: {exc}") from exc
    if resolved_parent != resolved_root:
        raise InputError(f"{label} parent resolves outside its owned root: {resolved_parent}")
    return path_abs


def remove_owned_workspace(path: Path) -> None:
    """Remove only the runner's exact workspaces/<run> tree after validating it."""
    workspace = Path(os.path.abspath(path))
    base = reject_linked_path_components(WORKSPACES_ROOT, "workspaces root")
    try:
        relative = workspace.relative_to(base)
    except ValueError as exc:
        raise InputError(f"refusing to clean outside the owned workspaces root: {workspace}") from exc
    if len(relative.parts) != 1:
        raise InputError(f"refusing to clean anything other than one owned run directory: {workspace}")
    reject_linked_path_components(workspace, "owned workspace")
    if not workspace.exists():
        return
    if not workspace.is_dir():
        raise InputError(f"owned workspace is not a directory: {workspace}")
    safe_tree(workspace)
    shutil.rmtree(workspace)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_tree(root: Path) -> dict[str, str]:
    """Hash every regular file and reject links/special entries anywhere."""
    reject_linked_path_components(root, "snapshot")
    if is_link_or_junction(root) or not root.is_dir():
        raise InputError(f"snapshot root is not a real directory: {root}")
    result: dict[str, str] = {}
    for current, dirs, files in os.walk(root, followlinks=False):
        base = Path(current)
        for name in list(dirs):
            path = base / name
            if is_link_or_junction(path):
                raise InputError(f"snapshot contains a symlink, junction, or reparse point: {path}")
        dirs.sort()
        for name in sorted(files):
            path = base / name
            if is_link_or_junction(path) or not path.is_file():
                raise InputError(f"snapshot contains a link or non-file: {path}")
            rel = path.relative_to(root).as_posix()
            if rel in result:
                raise InputError(f"duplicate snapshot path: {rel}")
            result[rel] = sha256(path)
    return result


def _no_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise InputError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_manifest(path: Path) -> dict[str, str]:
    reject_linked_path_components(path, "manifest")
    try:
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_no_duplicate_pairs)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise InputError(f"cannot read manifest {path}: {exc}") from exc
    if not isinstance(value, dict) or not value:
        raise InputError(f"manifest must be a nonempty path-to-SHA256 mapping: {path}")
    normalized: dict[str, str] = {}
    folded: set[str] = set()
    for raw, digest in value.items():
        if not isinstance(raw, str) or not raw or "\x00" in raw:
            raise InputError(f"invalid manifest path: {raw!r}")
        portable = raw.replace("\\", "/")
        parts = portable.split("/")
        if portable.startswith("/") or ":" in parts[0] or any(p in ("", ".", "..") for p in parts):
            raise InputError(f"manifest path must be normalized, relative, and contained: {raw}")
        key = "/".join(parts)
        case_key = os.path.normcase(key)
        if case_key in folded:
            raise InputError(f"duplicate case-insensitive manifest path: {key}")
        folded.add(case_key)
        if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdefABCDEF" for c in digest):
            raise InputError(f"invalid SHA256 for {key}")
        normalized[key] = digest.lower()
    return normalized


def validate_snapshot(root: Path, manifest_path: Path, label: str) -> dict[str, str]:
    reject_linked_path_components(root, f"{label} snapshot")
    if is_link_or_junction(root):
        raise InputError(f"{label} snapshot root must not be a symlink or junction")
    resolved = root.resolve(strict=True)
    if manifest_path.resolve(strict=True).is_relative_to(resolved):
        raise InputError(f"{label} manifest must be outside the snapshot tree")
    declared = read_manifest(manifest_path)
    observed = safe_tree(root)
    if observed != declared:
        missing = sorted(set(declared) - set(observed))
        extra = sorted(set(observed) - set(declared))
        changed = sorted(p for p in set(observed) & set(declared) if observed[p] != declared[p])
        raise InputError(f"{label} manifest/tree mismatch; missing={missing}, extra={extra}, changed={changed}")
    return observed


def validate_test_contract(test_file: Path, regression: dict[str, str]) -> None:
    try:
        tree = ast.parse(test_file.read_text(encoding="utf-8"), filename=str(test_file))
    except (OSError, UnicodeError, SyntaxError) as exc:
        raise InputError(f"selected regression test cannot be parsed: {exc}") from exc
    target = next(
        (node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == regression["method"]),
        None,
    )
    if target is None:
        raise InputError(f"selected regression is absent: {regression['method']}")
    has_edit = False
    has_refresh = False
    has_expected_assertion = False
    for node in ast.walk(target):
        if not isinstance(node, ast.Call):
            continue
        if isinstance(node.func, ast.Attribute) and node.func.attr == "edit_note":
            has_edit = any(isinstance(arg, ast.Constant) and arg.value == regression["expected_new"] for arg in node.args)
        if isinstance(node.func, ast.Attribute) and node.func.attr == "visible_workspace" and not node.args:
            has_refresh = True
        if isinstance(node.func, ast.Attribute) and node.func.attr == "assertEqual" and len(node.args) == 2:
            actual, expected = node.args
            is_report_note = (
                isinstance(actual, ast.Subscript)
                and isinstance(actual.value, ast.Subscript)
                and isinstance(actual.value.value, ast.Name)
                and actual.value.value.id == "view"
                and isinstance(actual.value.slice, ast.Constant)
                and actual.value.slice.value == "report"
                and isinstance(actual.slice, ast.Constant)
                and actual.slice.value == "note"
            )
            has_expected_assertion = (
                has_expected_assertion
                or (is_report_note and isinstance(expected, ast.Constant) and expected.value == regression["expected_new"])
            )
    if not (has_edit and has_refresh and has_expected_assertion):
        raise InputError("selected test must edit to the frozen note, refresh the workspace, and assert the report note")


def validate_existing_guards(original_test_file: Path, output_test_file: Path) -> None:
    try:
        original_tree = ast.parse(original_test_file.read_text(encoding="utf-8"))
        output_tree = ast.parse(output_test_file.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, SyntaxError) as exc:
        raise InputError(f"cannot validate unchanged original T1 tests: {exc}") from exc

    def methods(tree: ast.AST) -> dict[str, ast.FunctionDef]:
        return {node.name: node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}

    before, after = methods(original_tree), methods(output_tree)
    for name in ORIGINAL_GUARD_METHODS:
        if name not in before or name not in after:
            raise InputError(f"worker output removed an original T1 guard test: {name}")
        if ast.dump(before[name], include_attributes=False) != ast.dump(after[name], include_attributes=False):
            raise InputError(f"worker output changed an original T1 guard test: {name}")


def command_record(argv: list[str], cwd: Path, timeout_seconds: int, started: float,
                   completed: float | None, exit_code: int | None, timed_out: bool,
                   stdout_path: Path, stderr_path: Path) -> dict[str, Any]:
    return {
        "argv": argv,
        "cwd": str(cwd),
        "python": sys.version,
        "startedAt": datetime.fromtimestamp(started, timezone.utc).isoformat(),
        "completedAt": datetime.fromtimestamp(completed, timezone.utc).isoformat() if completed is not None else None,
        "durationSeconds": round(completed - started, 3) if completed is not None else None,
        "timeoutSeconds": timeout_seconds,
        "exitCode": exit_code,
        "timedOut": timed_out,
        "stdoutLog": str(stdout_path),
        "stderrLog": str(stderr_path),
    }


def run_command(name: str, cwd: Path, argv: list[str], results: Path, timeout: int) -> tuple[dict[str, Any], str, str]:
    started = time.time()
    timed_out = False
    exit_code: int | None = None
    completed: float | None = None
    try:
        proc = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)
        stdout, stderr, exit_code = proc.stdout, proc.stderr, proc.returncode
        completed = time.time()
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout.decode("utf-8", "replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr = exc.stderr.decode("utf-8", "replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "")
        timed_out = True
        completed = time.time()
    except OSError as exc:
        stdout, stderr = "", f"subprocess setup failed: {exc}"
        completed = time.time()
    stdout_path = results / f"{name}.stdout.log"
    stderr_path = results / f"{name}.stderr.log"
    stdout_path.write_text(stdout, encoding="utf-8")
    stderr_path.write_text(stderr, encoding="utf-8")
    return command_record(argv, cwd, timeout, started, completed, exit_code, timed_out, stdout_path, stderr_path), stdout, stderr


def test_result_is_expected_failure(stdout: str, stderr: str, test_id: str, old: str, new: str, count: int = 1) -> bool:
    transcript = stdout + "\n" + stderr
    return (
        f"{test_id}" in transcript
        and "FAIL:" in transcript
        and f"Ran {count} test" in transcript
        and "FAILED (failures=1)" in transcript
        and "errors=" not in transcript
        and f"AssertionError: '{old}' != '{new}'" in transcript
        and f"- {old}" in transcript
        and f"+ {new}" in transcript
    )


def test_result_is_pass(stdout: str, stderr: str, count: int = 1) -> bool:
    transcript = stdout + "\n" + stderr
    return f"Ran {count} test" in transcript and "OK" in transcript and "FAILED" not in transcript and "ERROR" not in transcript


def copy_arm(original: Path, output: Path, destination: Path, baseline: bool, source_hash: str, test_hash: str) -> None:
    shutil.copytree(original, destination)
    shutil.copy2(output / TEST_PATH, destination / TEST_PATH)
    if not baseline:
        shutil.copy2(output / SOURCE_PATH, destination / SOURCE_PATH)
    actual_source = sha256(destination / SOURCE_PATH)
    actual_test = sha256(destination / TEST_PATH)
    expected_source = source_hash if baseline else sha256(output / SOURCE_PATH)
    if actual_source != expected_source or actual_test != test_hash:
        raise InputError("disposable copy identity check failed")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog=("Frozen case saved-note-preview-after-edit selects tests/test_workspace.py::"
                "WorkspaceTests.test_editing_note_refreshes_report_preview. Expected original failure: "
                "report note is 'Initial note A' while the test expects 'Saved note A'. A generic nonzero "
                "exit does not count. Only the changed selected test and src/workspace.py are in scope."),
    )
    parser.add_argument("--original", type=Path, required=True, help="immutable original T1 snapshot directory")
    parser.add_argument("--original-manifest", type=Path, required=True, help="exact SHA256 manifest for original T1")
    parser.add_argument("--output", type=Path, required=True, help="frozen corrected T1 worker-output directory")
    parser.add_argument("--output-manifest", type=Path, required=True, help="exact SHA256 manifest for worker output")
    parser.add_argument("--regression", required=True, choices=sorted(REGRESSIONS),
                        help="frozen case: test_workspace.WorkspaceTests.test_editing_note_refreshes_report_preview; expected stale assertion: Initial note A vs Saved note A")
    parser.add_argument("--results", type=Path, required=True,
                        help="new retained result directory directly under .data/artifacts/regression-comparison/<run-id>")
    parser.add_argument("--timeout", type=int, default=30)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    results: Path | None = None
    workspaces: Path | None = None
    workspace_created = False
    payload: dict[str, Any] = {"status": "insufficient", "reason": "not_run"}
    exit_code = EXIT_INVALID
    try:
        args = parse_args(argv)
        if args.timeout < 1 or args.timeout > 300:
            raise InputError("timeout must be between 1 and 300 seconds")
        base_identity = validate_snapshot(args.original, args.original_manifest, "original")
        output_identity = validate_snapshot(args.output, args.output_manifest, "output")
        original = args.original.resolve(strict=True)
        output = args.output.resolve(strict=True)
        if base_identity.keys() != output_identity.keys():
            raise InputError("output file set differs from original fixture; undeclared behavior/config changes are rejected")
        changed = {p for p in base_identity if base_identity[p] != output_identity[p]}
        if not changed <= {SOURCE_PATH, TEST_PATH}:
            raise InputError(f"output changed files outside the selected T1 scope: {sorted(changed - {SOURCE_PATH, TEST_PATH})}")
        if TEST_PATH not in changed:
            raise InputError("output does not contain a changed selected regression test")
        regression = REGRESSIONS[args.regression]
        validate_test_contract(output / TEST_PATH, regression)
        validate_existing_guards(original / TEST_PATH, output / TEST_PATH)
        results = validate_new_run_directory(args.results, ARTIFACTS_ROOT, "results directory")
        workspaces = validate_new_run_directory(WORKSPACES_ROOT / results.name, WORKSPACES_ROOT, "workspaces directory")
        if results.name != workspaces.name:
            raise InputError("results and workspaces must use the same run ID")
        results.parent.mkdir(parents=True, exist_ok=True)
        results.mkdir()
        workspaces.parent.mkdir(parents=True, exist_ok=True)
        workspaces.mkdir()
        workspace_created = True
        baseline_dir = workspaces / "baseline"
        corrected_dir = workspaces / "corrected"
        regression_test_hash = output_identity[TEST_PATH]
        copy_arm(original, output, baseline_dir, True, base_identity[SOURCE_PATH], regression_test_hash)
        copy_arm(original, output, corrected_dir, False, base_identity[SOURCE_PATH], regression_test_hash)
        expected_baseline_tree = dict(base_identity)
        expected_baseline_tree[TEST_PATH] = regression_test_hash
        expected_corrected_tree = dict(output_identity)
        if safe_tree(baseline_dir) != expected_baseline_tree or safe_tree(corrected_dir) != expected_corrected_tree:
            raise InputError("disposable copy has a changed or missing source/config/fixture input")

        test_selector = regression["method"]
        named_command = [sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests", "-p", "test_workspace.py", "-k", test_selector, "-v"]
        full_command = [sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests", "-v"]
        records: dict[str, Any] = {}
        outcomes: dict[str, bool] = {}
        for arm, arm_dir in (("baseline", baseline_dir), ("corrected", corrected_dir)):
            for check, command in (("named", named_command), ("full", full_command)):
                name = f"{arm}-{check}"
                record, stdout, stderr = run_command(name, arm_dir, command, results, args.timeout)
                records[name] = record
                if check == "named":
                    outcomes[name] = (
                        record["exitCode"] == 1 and test_result_is_expected_failure(stdout, stderr, regression["test_id"], regression["expected_old"], regression["expected_new"])
                        if arm == "baseline" else record["exitCode"] == 0 and test_result_is_pass(stdout, stderr, 1)
                    )
                elif arm == "baseline":
                    outcomes[name] = record["exitCode"] == 1 and test_result_is_expected_failure(stdout, stderr, regression["test_id"], regression["expected_old"], regression["expected_new"], 3)
                else:
                    count = len([p for p in (corrected_dir / "tests").glob("test*.py") if p.is_file()])
                    # The frozen fixture currently contains three unittest methods in one file.
                    outcome = record["exitCode"] == 0 and "OK" in stdout + "\n" + stderr and "FAILED" not in stdout + "\n" + stderr and "ERROR" not in stdout + "\n" + stderr
                    outcomes[name] = bool(count and outcome and "Ran 3 tests" in stdout + "\n" + stderr)
        after_original = safe_tree(original)
        after_output = safe_tree(output)
        immutable = after_original == base_identity and after_output == output_identity
        verified = all(outcomes.values()) and immutable
        payload = {
            "status": "verified" if verified else "insufficient",
            "regression": args.regression,
            "retainedResultsDirectory": str(results),
            "disposableWorkspaceDirectory": str(workspaces),
            "original": {"path": str(original), "manifest": str(args.original_manifest.resolve()), "files": len(base_identity), "sourceSha256": base_identity[SOURCE_PATH]},
            "output": {"path": str(output), "manifest": str(args.output_manifest.resolve()), "files": len(output_identity), "changed": sorted(changed), "sourceSha256": output_identity[SOURCE_PATH]},
            "checks": records,
            "outcomes": outcomes,
            "inputsUnchangedAfterRun": immutable,
            "createdAt": datetime.now(timezone.utc).isoformat(),
            "python": sys.version,
        }
        exit_code = EXIT_VERIFIED if verified else EXIT_INSUFFICIENT
    except (InputError, OSError, RuntimeError, ValueError) as exc:
        payload = {"status": "insufficient", "reason": str(exc), "createdAt": datetime.now(timezone.utc).isoformat()}
        exit_code = EXIT_INVALID
    finally:
        # Keep every result artifact; clean only the exact runner-owned workspaces/<run-id> tree.
        cleanup = {"status": "not_created"}
        if workspaces is not None and workspace_created:
            try:
                remove_owned_workspace(workspaces)
                cleanup = {"status": "removed", "path": str(workspaces)}
            except (InputError, OSError) as exc:
                cleanup = {"status": "refused_or_failed", "path": str(workspaces), "reason": str(exc)}
                if payload.get("status") == "verified":
                    payload["status"] = "insufficient"
                    payload["reason"] = f"verified checks completed but disposable workspace cleanup failed: {exc}"
                    exit_code = EXIT_INSUFFICIENT
        if results is not None and results.is_dir():
            payload["workspaceCleanup"] = cleanup
            try:
                (results / "result.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            except OSError as exc:
                if payload.get("status") == "verified":
                    payload["status"] = "insufficient"
                    payload["reason"] = f"verified checks completed but retained result could not be finalized: {exc}"
                    exit_code = EXIT_INSUFFICIENT
    summary = {
        "status": payload.get("status"),
        "regression": payload.get("regression"),
        "outcomes": payload.get("outcomes"),
        "inputsUnchangedAfterRun": payload.get("inputsUnchangedAfterRun"),
        "results": payload.get("retainedResultsDirectory"),
        "workspaceCleanup": payload.get("workspaceCleanup"),
    }
    if payload.get("reason"):
        summary["reason"] = payload["reason"]
    print(json.dumps(summary, separators=(",", ":"), ensure_ascii=False))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
