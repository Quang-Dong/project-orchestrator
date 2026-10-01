import unittest

from src.checklist_export import export_checklist


class ChecklistExportTests(unittest.TestCase):
    def test_old_done_marker_is_omitted(self):
        self.assertEqual(
            export_checklist([{"label": "Old item", "status": "done"}]),
            [],
        )

    def test_active_item_is_included(self):
        self.assertEqual(
            export_checklist([{"label": "Call home", "status": "active"}]),
            ["Call home"],
        )


if __name__ == "__main__":
    unittest.main()
