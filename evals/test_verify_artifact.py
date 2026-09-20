import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "skills" / "project-orchestrator" / "scripts" / "verify_artifact.py"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


class VerifyArtifactCliTests(unittest.TestCase):
    def run_cli(self, root: Path, manifest: Path) -> tuple[int, dict, str]:
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "--root", str(root), "--manifest", str(manifest)],
            check=False,
            capture_output=True,
            text=True,
        )
        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError as exc:  # pragma: no cover - makes a contract failure obvious
            self.fail(f"stdout was not JSON: {result.stdout!r}; stderr={result.stderr!r}; error={exc}")
        self.assertEqual(result.stderr, "")
        self.assertEqual(set(payload), {"errors", "files", "manifest", "root", "status"})
        return result.returncode, payload, result.stdout

    def write_manifest(self, path: Path, value: object) -> None:
        path.write_text(json.dumps(value), encoding="utf-8")

    def test_verified_mapping_is_sorted_deterministic_and_read_only(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "artifact"
            root.mkdir()
            first = root / "a.txt"
            second = root / "z.txt"
            first.write_text("alpha", encoding="utf-8")
            second.write_text("zeta", encoding="utf-8")
            manifest = base / "manifest.json"
            self.write_manifest(manifest, {"z.txt": sha256(second), "a.txt": sha256(first)})
            before = {
                path.relative_to(base).as_posix(): sha256(path) if path.is_file() else None
                for path in base.rglob("*")
            }

            first_run = self.run_cli(root, manifest)
            second_run = self.run_cli(root, manifest)

            self.assertEqual(first_run[0], 0)
            self.assertEqual(first_run[1]["status"], "verified")
            self.assertEqual([entry["path"] for entry in first_run[1]["files"]], ["a.txt", "z.txt"])
            self.assertEqual(first_run[2], second_run[2])
            self.assertNotIn("accepted", first_run[2])
            after = {
                path.relative_to(base).as_posix(): sha256(path) if path.is_file() else None
                for path in base.rglob("*")
            }
            self.assertEqual(before, after)
            self.assertNotIn("__pycache__", after)

    def test_release_mapping_inside_root_and_path_list_are_supported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "artifact"
            root.mkdir()
            item = root / "one.txt"
            item.write_text("one", encoding="utf-8")

            inside_manifest = root / "manifest.json"
            self.write_manifest(inside_manifest, {"schemaVersion": 2, "files": {"one.txt": sha256(item)}})
            code, payload, _ = self.run_cli(root, inside_manifest)
            self.assertEqual(code, 0)
            self.assertEqual(payload["status"], "verified")
            self.assertEqual([entry["path"] for entry in payload["files"]], ["one.txt"])

            list_manifest = base / "list.json"
            self.write_manifest(list_manifest, [{"path": "one.txt", "sha256": sha256(item)}])
            code, payload, _ = self.run_cli(root, list_manifest)
            self.assertEqual(code, 0)
            self.assertEqual(payload["status"], "verified")

    def test_missing_and_hash_mismatch_are_mismatch_exit_one(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "artifact"
            root.mkdir()
            present = root / "present.txt"
            present.write_text("actual", encoding="utf-8")
            manifest = base / "manifest.json"
            self.write_manifest(
                manifest,
                {"missing.txt": hashlib.sha256(b"missing").hexdigest(), "present.txt": "0" * 64},
            )

            code, payload, _ = self.run_cli(root, manifest)

            self.assertEqual(code, 1)
            self.assertEqual(payload["status"], "mismatch")
            self.assertEqual([entry["path"] for entry in payload["files"]], ["missing.txt", "present.txt"])
            self.assertEqual([entry["status"] for entry in payload["files"]], ["missing", "mismatch"])
            self.assertEqual(
                [entry["error"]["code"] for entry in payload["files"]],
                ["missing_file", "hash_mismatch"],
            )

    def test_invalid_manifest_shapes_and_duplicate_paths_are_invalid_exit_two(self) -> None:
        cases = [
            ("malformed", "{"),
            ("empty_list", "[]"),
            ("empty_mapping", "{}"),
            ("unsupported_shape", "42"),
            (
                "duplicate_normalized_paths",
                json.dumps({"dir\\file.txt": "0" * 64, "dir/file.txt": "0" * 64}),
            ),
            ("invalid_hash", json.dumps({"file.txt": "not-a-sha256"})),
            ("missing_hash", json.dumps([{"path": "file.txt"}])),
            ("duplicate_key", '{"file.txt":"' + "0" * 64 + '","file.txt":"' + "1" * 64 + '"}'),
            ("parent_escape", json.dumps({"../file.txt": "0" * 64})),
        ]
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "artifact"
            root.mkdir()
            for name, content in cases:
                with self.subTest(name=name):
                    manifest = base / f"{name}.json"
                    manifest.write_text(content, encoding="utf-8")
                    code, payload, _ = self.run_cli(root, manifest)
                    self.assertEqual(code, 2)
                    self.assertEqual(payload["status"], "invalid")
                    self.assertTrue(payload["errors"])

    def test_absolute_manifest_entry_and_declared_manifest_are_invalid(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "artifact"
            root.mkdir()
            outside = base / "outside.txt"
            outside.write_text("outside", encoding="utf-8")

            absolute_manifest = base / "absolute.json"
            self.write_manifest(absolute_manifest, {str(outside): sha256(outside)})
            code, payload, _ = self.run_cli(root, absolute_manifest)
            self.assertEqual(code, 2)
            self.assertEqual(payload["status"], "invalid")
            self.assertEqual(payload["errors"][0]["code"], "absolute_path")

            inside_manifest = root / "self.json"
            self.write_manifest(inside_manifest, {"self.json": "0" * 64})
            code, payload, _ = self.run_cli(root, inside_manifest)
            self.assertEqual(code, 2)
            self.assertEqual(payload["status"], "invalid")
            self.assertEqual(payload["errors"][0]["code"], "manifest_declared")

    def test_invalid_root_and_manifest_inputs_are_invalid_exit_two(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root_file = base / "root.txt"
            root_file.write_text("not a directory", encoding="utf-8")
            valid_manifest = base / "manifest.json"
            self.write_manifest(valid_manifest, {"file.txt": "0" * 64})

            code, payload, _ = self.run_cli(root_file, valid_manifest)
            self.assertEqual(code, 2)
            self.assertEqual(payload["errors"][0]["code"], "root_not_directory")

            missing_manifest = base / "missing.json"
            code, payload, _ = self.run_cli(base, missing_manifest)
            self.assertEqual(code, 2)
            self.assertEqual(payload["errors"][0]["code"], "manifest_not_file")

    def test_symlink_escape_is_invalid_when_symlinks_are_available(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "artifact"
            root.mkdir()
            outside = base / "outside.txt"
            outside.write_text("outside", encoding="utf-8")
            link = root / "link.txt"
            try:
                os.symlink(outside, link)
            except (OSError, NotImplementedError) as exc:
                self.skipTest(f"symlink unavailable in this runtime: {exc}")

            manifest = base / "manifest.json"
            self.write_manifest(manifest, {"link.txt": sha256(outside)})
            code, payload, _ = self.run_cli(root, manifest)
            self.assertEqual(code, 2)
            self.assertEqual(payload["status"], "invalid")
            self.assertEqual(payload["errors"][0]["code"], "path_escape")


if __name__ == "__main__":
    unittest.main()
