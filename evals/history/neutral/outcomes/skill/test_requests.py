import unittest
from requests import attention_today

class ExistingChecks(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(attention_today([], "2026-03-15"), [])
    def test_input_unchanged(self):
        rows = [{"id": "a", "status": "open", "due_date": "2026-03-14"}]
        self.assertEqual(attention_today(rows, "2026-03-15"), rows)
        self.assertEqual(rows[0]["due_date"], "2026-03-14")

    def test_returns_actionable_due_and_overdue_requests_in_input_order(self):
        rows = [
            {"id": "future", "status": "open", "due_date": "2026-03-16"},
            {"id": "today", "status": "open", "due_date": "2026-03-15"},
            {"id": "overdue", "status": "in_progress", "due_date": "2026-03-14"},
        ]
        self.assertEqual(
            [item["id"] for item in attention_today(rows, "2026-03-15")],
            ["today", "overdue"],
        )

    def test_excludes_terminal_and_undated_requests(self):
        rows = [
            {"id": "completed", "status": "completed", "due_date": "2026-03-15"},
            {"id": "cancelled", "status": "cancelled", "due_date": "2026-03-14"},
            {"id": "undated", "status": "open", "due_date": None},
        ]
        self.assertEqual(attention_today(rows, "2026-03-15"), [])

if __name__ == "__main__":
    unittest.main()
