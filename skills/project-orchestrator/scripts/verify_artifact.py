#!/usr/bin/env python3
"""Verify a declared, read-only artifact manifest against a directory."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Iterable


EXIT_VERIFIED = 0
EXIT_MISMATCH = 1
EXIT_INVALID = 2
SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")


class InvalidManifest(Exception):
    def __init__(self, code: str, message: str, path: str | None = None) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.path = path


class DuplicateJsonKey(Exception):
    def __init__(self, key: str) -> None:
        super().__init__(key)
        self.key = key


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise InvalidManifest("arguments", message)


def error_object(code: str, message: str, path: str | None = None) -> dict[str, str]:
    value = {"code": code, "message": message}
    if path is not None:
        value["path"] = path
    return value


def output_payload(
    status: str,
    root: str,
    manifest: str,
    files: Iterable[dict[str, Any]] = (),
    errors: Iterable[dict[str, Any]] = (),
) -> dict[str, Any]:
    ordered_files = sorted(files, key=lambda item: item["path"])
    ordered_errors = sorted(
        errors,
        key=lambda item: (item.get("code", ""), item.get("path", ""), item.get("message", "")),
    )
    return {
        "status": status,
        "root": root,
        "manifest": manifest,
        "files": ordered_files,
        "errors": ordered_errors,
    }


def emit(payload: dict[str, Any], exit_code: int) -> int:
    sys.stdout.write(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")
    return exit_code


def duplicate_rejecting_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJsonKey(key)
        result[key] = value
    return result


def normalize_relative_path(raw_path: Any) -> tuple[str, str]:
    if not isinstance(raw_path, str):
        raise InvalidManifest("path_type", "manifest path must be a string")
    if not raw_path:
        raise InvalidManifest("empty_path", "manifest path must not be empty")
    if "\x00" in raw_path:
        raise InvalidManifest("nul_path", "manifest path contains a NUL character", raw_path)

    portable = raw_path.replace("\\", "/")
    if portable.startswith("/") or re.match(r"^[A-Za-z]:", portable):
        raise InvalidManifest("absolute_path", "manifest path must be relative", raw_path)

    parts: list[str] = []
    for part in portable.split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            if not parts:
                raise InvalidManifest("path_escape", "manifest path escapes the artifact root", raw_path)
            parts.pop()
            continue
        parts.append(part)

    if not parts:
        raise InvalidManifest("empty_path", "manifest path must name a file", raw_path)
    normalized = "/".join(parts)
    return normalized, os.path.normcase(normalized)


def root_and_resolved_path(root_argument: str) -> tuple[Path, Path]:
    root = Path(root_argument)
    try:
        resolved = root.resolve(strict=False)
    except (OSError, RuntimeError) as exc:
        raise InvalidManifest("root_resolution", f"cannot resolve artifact root: {exc}") from exc
    if not root.is_dir():
        raise InvalidManifest("root_not_directory", "artifact root must be an existing directory")
    return root, resolved


def manifest_path(manifest_argument: str) -> tuple[Path, Path]:
    manifest = Path(manifest_argument)
    try:
        resolved = manifest.resolve(strict=False)
    except (OSError, RuntimeError) as exc:
        raise InvalidManifest("manifest_resolution", f"cannot resolve manifest: {exc}") from exc
    if not manifest.is_file():
        raise InvalidManifest("manifest_not_file", "manifest must be an existing file")
    return manifest, resolved


def inside_root_key(root_resolved: Path, candidate_resolved: Path) -> str | None:
    try:
        relative = candidate_resolved.relative_to(root_resolved)
    except ValueError:
        return None
    _, key = normalize_relative_path(relative.as_posix())
    return key


def read_manifest(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
        return json.loads(text, object_pairs_hook=duplicate_rejecting_object)
    except DuplicateJsonKey as exc:
        raise InvalidManifest("duplicate_json_key", f"manifest contains duplicate JSON key: {exc.key}") from exc
    except (OSError, UnicodeError) as exc:
        raise InvalidManifest("manifest_read", f"cannot read manifest: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise InvalidManifest("malformed_json", f"manifest is not valid JSON: {exc.msg}") from exc


def entries_from_manifest(value: Any) -> list[tuple[Any, Any]]:
    if isinstance(value, list):
        if not value:
            raise InvalidManifest("empty_manifest", "manifest list must not be empty")
        entries: list[tuple[Any, Any]] = []
        for item in value:
            if not isinstance(item, dict) or "path" not in item or "sha256" not in item:
                raise InvalidManifest("unsupported_shape", "list entries require path and sha256 fields")
            entries.append((item["path"], item["sha256"]))
        return entries

    if not isinstance(value, dict):
        raise InvalidManifest("unsupported_shape", "manifest must be a mapping or list")

    if "files" in value:
        files = value["files"]
        if not isinstance(files, dict):
            raise InvalidManifest("unsupported_shape", "manifest files field must be a mapping")
        value = files

    if not value:
        raise InvalidManifest("empty_manifest", "manifest mapping must not be empty")
    return list(value.items())


def validate_entries(
    raw_entries: list[tuple[Any, Any]],
    root_resolved: Path,
    manifest_resolved: Path,
) -> list[tuple[str, str, Path]]:
    manifest_key = inside_root_key(root_resolved, manifest_resolved)
    seen: set[str] = set()
    entries: list[tuple[str, str, Path]] = []
    for raw_path, expected in raw_entries:
        normalized, key = normalize_relative_path(raw_path)
        if key in seen:
            raise InvalidManifest("duplicate_path", "manifest contains duplicate paths after normalization", normalized)
        seen.add(key)
        if manifest_key is not None and key == manifest_key:
            raise InvalidManifest("manifest_declared", "the control manifest cannot be an artifact entry", normalized)
        if not isinstance(expected, str) or not SHA256_RE.fullmatch(expected):
            raise InvalidManifest("invalid_sha256", "manifest sha256 must be a 64-character hexadecimal string", normalized)
        candidate = root_resolved.joinpath(*normalized.split("/"))
        try:
            resolved_candidate = candidate.resolve(strict=False)
        except (OSError, RuntimeError) as exc:
            raise InvalidManifest("path_resolution", f"cannot resolve artifact path: {exc}", normalized) from exc
        try:
            resolved_candidate.relative_to(root_resolved)
        except ValueError as exc:
            raise InvalidManifest("path_escape", "artifact path resolves outside the root", normalized) from exc
        entries.append((normalized, expected.lower(), candidate))
    return entries


def verify_entries(entries: list[tuple[str, str, Path]]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for normalized, expected, candidate in entries:
        if not candidate.is_file():
            results.append(
                {
                    "path": normalized,
                    "status": "missing",
                    "expectedSha256": expected,
                    "actualSha256": None,
                    "error": error_object("missing_file", "declared artifact file is missing or not a file", normalized),
                }
            )
            continue
        try:
            digest = hashlib.sha256()
            with candidate.open("rb") as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    digest.update(chunk)
            actual = digest.hexdigest()
        except OSError as exc:
            results.append(
                {
                    "path": normalized,
                    "status": "mismatch",
                    "expectedSha256": expected,
                    "actualSha256": None,
                    "error": error_object("file_read", f"cannot read declared artifact file: {exc}", normalized),
                }
            )
            continue
        if actual != expected:
            results.append(
                {
                    "path": normalized,
                    "status": "mismatch",
                    "expectedSha256": expected,
                    "actualSha256": actual,
                    "error": error_object("hash_mismatch", "artifact SHA-256 does not match", normalized),
                }
            )
        else:
            results.append(
                {
                    "path": normalized,
                    "status": "verified",
                    "expectedSha256": expected,
                    "actualSha256": actual,
                    "error": None,
                }
            )
    return sorted(results, key=lambda item: item["path"])


def parser() -> argparse.ArgumentParser:
    command = JsonArgumentParser(description=__doc__)
    command.add_argument("--root", required=True)
    command.add_argument("--manifest", required=True)
    return command


def main(argv: list[str] | None = None) -> int:
    root_label = ""
    manifest_label = ""
    try:
        args = parser().parse_args(argv)
        root_label = args.root
        manifest_label = args.manifest
        root, root_resolved = root_and_resolved_path(args.root)
        manifest, manifest_resolved = manifest_path(args.manifest)
        manifest_value = read_manifest(manifest)
        entries = validate_entries(entries_from_manifest(manifest_value), root_resolved, manifest_resolved)
        files = verify_entries(entries)
        status = "mismatch" if any(item["status"] != "verified" for item in files) else "verified"
        return emit(
            output_payload(status, str(root), str(manifest), files=files),
            EXIT_MISMATCH if status == "mismatch" else EXIT_VERIFIED,
        )
    except InvalidManifest as exc:
        return emit(
            output_payload(
                "invalid",
                root_label,
                manifest_label,
                errors=[error_object(exc.code, exc.message, exc.path)],
            ),
            EXIT_INVALID,
        )


if __name__ == "__main__":
    raise SystemExit(main())
