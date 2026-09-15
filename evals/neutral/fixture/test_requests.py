import unittest
from requests import attention_today

class ExistingChecks(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(attention_today([], "2026-03-15"), [])
    def test_input_unchanged(self):
        rows = [{"id": "a", "status": "open", "due_date": "2026-03-14"}]
        self.assertEqual(attention_today(rows, "2026-03-15"), rows)
        self.assertEqual(rows[0]["due_date"], "2026-03-14")

if __name__ == "__main__":
    unittest.main()
