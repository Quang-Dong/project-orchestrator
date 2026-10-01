import unittest

from src.workspace import Workspace


class WorkspaceTests(unittest.TestCase):
    def test_selection_updates_editor_and_report_for_each_learner(self):
        workspace = Workspace()
        workspace.select_learner("learner-b")
        view = workspace.visible_workspace()
        self.assertEqual(view["learner"], "Blair")
        self.assertEqual(view["editor_note"], "Initial note B")
        self.assertEqual(view["report"]["learner"], "Blair")
        self.assertEqual(view["report"]["note"], "Initial note B")

        workspace.select_learner("learner-a")
        view = workspace.visible_workspace()
        self.assertEqual(view["learner"], "Avery")
        self.assertEqual(view["report"]["note"], "Initial note A")

    def test_reopening_a_preview_without_source_changes_is_stable(self):
        workspace = Workspace()
        first = workspace.visible_workspace()
        second = workspace.visible_workspace()
        self.assertEqual(first, second)

    def test_editing_note_refreshes_report_preview(self):
        workspace = Workspace()
        workspace.visible_workspace()

        workspace.edit_note("Saved note A")
        view = workspace.visible_workspace()

        self.assertEqual(view["editor_note"], "Saved note A")
        self.assertEqual(view["report"]["note"], "Saved note A")


if __name__ == "__main__":
    unittest.main()
