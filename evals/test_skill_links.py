import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


SKILL_ROOT = Path(__file__).resolve().parents[1] / "skills/project-orchestrator"


def heading_slug(title: str) -> str:
    title = re.sub(r"[`*_]", "", title).strip().lower()
    return re.sub(r"[^\w -]", "", title).replace(" ", "-")


class SkillLinkTests(unittest.TestCase):
    def test_local_markdown_links_resolve_to_files_and_headings(self):
        for source in SKILL_ROOT.rglob("*.md"):
            content = source.read_text(encoding="utf-8")
            for raw_target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", content):
                target = raw_target.split(maxsplit=1)[0].strip("<>")
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc:
                    continue

                relative_path = unquote(parsed.path)
                destination = (source.parent / relative_path).resolve() if relative_path else source
                with self.subTest(source=source.relative_to(SKILL_ROOT), target=target):
                    self.assertTrue(destination.is_file())
                    if parsed.fragment:
                        headings = {
                            heading_slug(title)
                            for title in re.findall(
                                r"^#{1,6}\s+(.+?)\s*#*\s*$",
                                destination.read_text(encoding="utf-8"),
                                re.M,
                            )
                        }
                        self.assertIn(unquote(parsed.fragment).lower(), headings)


if __name__ == "__main__":
    unittest.main()
