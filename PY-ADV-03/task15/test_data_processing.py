# PY-ADV-03 - Task 15
# Unit Tests for Data-Processing Functions

import unittest


def validate_score(score):
    """Validate whether a score is between 0 and 100."""

    if isinstance(score, bool):
        return False

    if not isinstance(score, (int, float)):
        return False

    return 0 <= score <= 100


def calculate_grade(score):
    """Calculate grade based on score."""

    if not validate_score(score):
        return "Invalid"

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def clean_name(name):
    """Clean and normalize a student name."""

    if name is None or not isinstance(name, str):
        return "Unknown"

    name = name.strip()

    if not name:
        return "Unknown"

    return name.title()


def transform_student(student):
    """Transform a student record."""

    return {
        "name": clean_name(student.get("name")),
        "score": student.get("score"),
        "grade": calculate_grade(student.get("score"))
    }


class TestDataProcessing(unittest.TestCase):

    def test_valid_score(self):
        self.assertTrue(validate_score(85))

    def test_zero_score(self):
        self.assertTrue(validate_score(0))

    def test_maximum_score(self):
        self.assertTrue(validate_score(100))

    def test_invalid_high_score(self):
        self.assertFalse(validate_score(101))

    def test_invalid_negative_score(self):
        self.assertFalse(validate_score(-1))

    def test_invalid_score_type(self):
        self.assertFalse(validate_score("85"))

    def test_grade_a(self):
        self.assertEqual(calculate_grade(95), "A")

    def test_grade_b(self):
        self.assertEqual(calculate_grade(85), "B")

    def test_grade_c(self):
        self.assertEqual(calculate_grade(75), "C")

    def test_grade_d(self):
        self.assertEqual(calculate_grade(65), "D")

    def test_grade_f(self):
        self.assertEqual(calculate_grade(50), "F")

    def test_invalid_grade(self):
        self.assertEqual(calculate_grade(150), "Invalid")

    def test_clean_name(self):
        self.assertEqual(clean_name("  teja  "), "Teja")

    def test_empty_name(self):
        self.assertEqual(clean_name(""), "Unknown")

    def test_none_name(self):
        self.assertEqual(clean_name(None), "Unknown")

    def test_transform_student(self):
        student = {
            "name": "  teja ",
            "score": 85
        }

        expected = {
            "name": "Teja",
            "score": 85,
            "grade": "B"
        }

        self.assertEqual(
            transform_student(student),
            expected
        )


if __name__ == "__main__":
    print("=== PY-ADV-03 Task 15 ===")
    print("Running unit tests...\n")

    unittest.main(verbosity=2)