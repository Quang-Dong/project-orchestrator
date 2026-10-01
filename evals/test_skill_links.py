import re
import unittest
from pathlib import Path, PurePosixPath, PureWindowsPath
from urllib.parse import unquote, urlsplit


SKILL_ROOT = Path(__file__).resolve().parents[1] / "skills/project-orchestrator"
REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def heading_slug(title: str) -> str:
    title = re.sub(r"[`*_]", "", title).strip().lower()
    return re.sub(r"[^\w -]", "", title).replace(" ", "-")


def validate_local_link(
    package_root: Path,
    source: Path,
    target: str,
    *,
    allow_directory: bool = False,
) -> None:
    """Require local Markdown targets to resolve inside the selected root."""
    parsed = urlsplit(target)
    if PureWindowsPath(target).is_absolute() or PurePosixPath(target).is_absolute():
        raise AssertionError(f"local link uses an absolute path: {target}")
    if parsed.scheme.lower() == "file":
        raise AssertionError(f"local link uses a file URI: {target}")
    if parsed.scheme or parsed.netloc:
        return

    relative_path = unquote(parsed.path)
    if relative_path and (
        PurePosixPath(relative_path).is_absolute()
        or PureWindowsPath(relative_path).is_absolute()
    ):
        raise AssertionError(f"local link uses an absolute path: {target}")

    root = package_root.resolve()
    source = source.resolve()
    if not source.is_relative_to(root):
        raise AssertionError(f"link source is outside package: {source}")

    destination = (source.parent / relative_path).resolve() if relative_path else source
    if not destination.is_relative_to(root):
        raise AssertionError(f"link escapes package: {target}")
    if not destination.is_file() and not (allow_directory and destination.is_dir()):
        raise AssertionError(f"linked file does not exist: {target}")

    if parsed.fragment:
        if destination.is_dir():
            destination = destination / "README.md"
        if not destination.is_file():
            raise AssertionError(f"linked heading has no Markdown file: {target}")
        headings = {
            heading_slug(title)
            for title in re.findall(
                r"^#{1,6}\s+(.+?)\s*#*\s*$",
                destination.read_text(encoding="utf-8"),
                re.M,
            )
        }
        fragment = unquote(parsed.fragment).lower()
        if fragment not in headings:
            raise AssertionError(f"linked heading does not exist: {target}")


class SkillLinkTests(unittest.TestCase):
    def test_package_markdown_links_resolve_to_files_and_headings(self):
        for source in SKILL_ROOT.rglob("*.md"):
            content = source.read_text(encoding="utf-8")
            for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", content):
                target = target.split(maxsplit=1)[0].strip("<>")
                with self.subTest(source=source.relative_to(SKILL_ROOT), target=target):
                    validate_local_link(SKILL_ROOT, source, target)

    def test_repository_maintainer_markdown_links_resolve(self):
        sources = [REPOSITORY_ROOT / "README.md"]
        sources.extend(
            path
            for path in (REPOSITORY_ROOT / "evals").rglob("*.md")
            if "fixtures" not in path.relative_to(REPOSITORY_ROOT).parts
            and "outcomes" not in path.relative_to(REPOSITORY_ROOT).parts
        )
        for source in sorted(set(sources)):
            content = source.read_text(encoding="utf-8")
            for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", content):
                target = target.split(maxsplit=1)[0].strip("<>")
                with self.subTest(
                    source=source.relative_to(REPOSITORY_ROOT), target=target
                ):
                    validate_local_link(
                        REPOSITORY_ROOT, source, target, allow_directory=True
                    )

    def test_fixture_accepts_valid_relative_file_and_anchor(self):
        with TemporaryPackage() as package:
            source = package.write("references/start.md", "[guide](guide.md#use-it)\n")
            package.write("references/guide.md", "# Use it\n")
            validate_local_link(package.root, source, "guide.md#use-it")

    def test_fixture_rejects_missing_file_and_anchor(self):
        with TemporaryPackage() as package:
            source = package.write("start.md", "# Start\n")
            for target in ("missing.md", "start.md#not-here"):
                with self.subTest(target=target), self.assertRaises(AssertionError):
                    validate_local_link(package.root, source, target)

    def test_directory_links_are_opt_in_and_keep_missing_target_and_anchor_checks(self):
        with TemporaryPackage() as package:
            source = package.write("start.md", "# Start\n")
            docs = package.root / "docs"
            docs.mkdir()
            (docs / "README.md").write_text("# Archive\n", encoding="utf-8")

            with self.assertRaises(AssertionError):
                validate_local_link(package.root, source, "docs/")

            validate_local_link(
                package.root, source, "docs/#archive", allow_directory=True
            )
            for target in ("missing/", "docs/#missing"):
                with self.subTest(target=target), self.assertRaises(AssertionError):
                    validate_local_link(
                        package.root, source, target, allow_directory=True
                    )

    def test_fixture_rejects_traversal_and_absolute_paths_even_when_file_exists(self):
        with TemporaryPackage() as package:
            source = package.write("nested/start.md", "# Start\n")
            escaped = package.root.parent / "outside.md"
            escaped.write_text("# Outside\n", encoding="utf-8")
            absolute_targets = (str(escaped),)
            try:
                for target in ("../../outside.md", *absolute_targets):
                    with self.subTest(target=target), self.assertRaises(AssertionError):
                        validate_local_link(package.root, source, target)
            finally:
                escaped.unlink(missing_ok=True)

    def test_fixture_rejects_file_uris(self):
        with TemporaryPackage() as package:
            source = package.write("start.md", "# Start\n")
            escaped = package.root.parent / "outside.md"
            escaped.write_text("# Outside\n", encoding="utf-8")
            targets = (escaped.as_uri(), "file://server/share/outside.md")
            try:
                for target in targets:
                    with self.subTest(target=target), self.assertRaises(AssertionError):
                        validate_local_link(package.root, source, target)
            finally:
                escaped.unlink(missing_ok=True)

    def test_fixture_rejects_symlink_escape_when_supported(self):
        with TemporaryPackage() as package:
            source = package.write("start.md", "# Start\n")
            escaped = package.root.parent / "outside.md"
            escaped.write_text("# Outside\n", encoding="utf-8")
            link = package.root / "outside-link.md"
            try:
                try:
                    link.symlink_to(escaped)
                except (OSError, NotImplementedError) as error:
                    self.skipTest(f"creating symlinks is unavailable: {error}")
                with self.assertRaises(AssertionError):
                    validate_local_link(package.root, source, "outside-link.md")
            finally:
                link.unlink(missing_ok=True)
                escaped.unlink(missing_ok=True)


class TemporaryPackage:
    def __init__(self):
        import tempfile

        self._temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self._temporary_directory.name).resolve()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self._temporary_directory.cleanup()

    def write(self, relative_path: str, content: str) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path


if __name__ == "__main__":
    unittest.main()
