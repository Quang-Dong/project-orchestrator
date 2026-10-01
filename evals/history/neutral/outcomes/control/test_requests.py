import unittest
from requests import attention_today

class ExistingChecks(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(attention_today([], "2026-03-15"), [])
    def test_input_unchanged(self):
        rows = [{"id": "a", "status": "open", "due_date": "2026-03-14"}]
        self.assertEqual(attention_today(rows, "2026-03-15"), rows)
        self.assertEqual(rows[0]["due_date"], "2026-03-14")

    def test_returns_due_open_and_in_progress_requests_in_input_order(self):
        rows = [
            {"id": "future", "status": "open", "due_date": "2026-03-16"},
            {"id": "in-progress", "status": "in_progress", "due_date": "2026-03-14"},
            {"id": "today", "status": "open", "due_date": "2026-03-15"},
            {"id": "overdue", "status": "open", "due_date": "2026-03-10"},
        ]

        self.assertEqual(
            attention_today(rows, "2026-03-15"),
            [rows[1], rows[2], rows[3]],
        )

    def test_excludes_undated_completed_and_cancelled_requests(self):
        rows = [
            {"id": "undated-open", "status": "open", "due_date": None},
            {"id": "undated-progress", "status": "in_progress", "due_date": None},
            {"id": "completed", "status": "completed", "due_date": "2026-03-15"},
            {"id": "cancelled", "status": "cancelled", "due_date": "2026-03-15"},
        ]

        self.assertEqual(attention_today(rows, "2026-03-15"), [])

if __name__ == "__main__":
    unittest.main()
