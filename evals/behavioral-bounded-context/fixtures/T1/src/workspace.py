"""Small synthetic model of a teacher workspace's saved notes and report view."""


class Workspace:
    def __init__(self, learners=None, notes=None):
        self.learners = learners or {"learner-a": "Avery", "learner-b": "Blair"}
        self.notes = notes or {"learner-a": "Initial note A", "learner-b": "Initial note B"}
        self.selected_learner_id = "learner-a"
        self._report_cache = {}

    def select_learner(self, learner_id):
        if learner_id not in self.learners:
            raise KeyError(learner_id)
        self.selected_learner_id = learner_id

    def edit_note(self, text):
        self.notes[self.selected_learner_id] = text

    def report_preview(self):
        """Build a report preview using the currently selected learner's note."""
        learner_id = self.selected_learner_id
        if learner_id not in self._report_cache:
            self._report_cache[learner_id] = {
                "learner": self.learners[learner_id],
                "note": self.notes[learner_id],
            }
        return dict(self._report_cache[learner_id])

    def visible_workspace(self):
        """Return the editor and report panels currently visible to the teacher."""
        learner_id = self.selected_learner_id
        return {
            "learner": self.learners[learner_id],
            "editor_note": self.notes[learner_id],
            "report": self.report_preview(),
        }
