import unittest

from src.labels import display_class_title


class LabelTests(unittest.TestCase):
    def test_class_title_is_shown_without_outer_whitespace(self):
        self.assertEqual(display_class_title("  Reading group  "), "Reading group")

    def test_title_text_is_preserved(self):
        self.assertEqual(display_class_title("Year 8"), "Year 8")


if __name__ == "__main__":
    unittest.main()
