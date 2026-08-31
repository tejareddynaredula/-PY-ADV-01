import unittest

from app.exceptions.student_exceptions import StudentNotFoundError
from app.models.student import Student
from app.services.student_service import StudentService
from app.utils.helpers import find_student_by_id


class TestStudentManagement(unittest.TestCase):
    """Test Student Management System functionality."""

    def setUp(self):
        self.student = Student(1, "Teja", 22, "Python")
        self.service = StudentService()

    def test_student_creation(self):
        self.assertEqual(self.student.student_id, 1)
        self.assertEqual(self.student.name, "Teja")

    def test_add_student(self):
        self.service.add_student(self.student)
        self.assertEqual(len(self.service.get_students()), 1)

    def test_find_student(self):
        self.service.add_student(self.student)
        result = find_student_by_id(self.service.get_students(), 1)
        self.assertEqual(result.name, "Teja")

    def test_student_not_found(self):
        result = find_student_by_id(self.service.get_students(), 99)
        self.assertIsNone(result)

    def test_update_student(self):
        self.service.add_student(self.student)

        self.service.update_student(
            1,
            "Teja Reddy",
            23,
            "AI/ML",
        )

        student = self.service.get_students()[0]

        self.assertEqual(student.name, "Teja Reddy")
        self.assertEqual(student.age, 23)
        self.assertEqual(student.course, "AI/ML")

    def test_update_student_not_found(self):
        with self.assertRaises(StudentNotFoundError):
            self.service.update_student(
                99,
                "Test",
                20,
                "Python",
            )

    def test_delete_student(self):
        self.service.add_student(self.student)

        self.service.delete_student(1)

        self.assertEqual(len(self.service.get_students()), 0)

    def test_delete_student_not_found(self):
        with self.assertRaises(StudentNotFoundError):
            self.service.delete_student(99)

    def test_invalid_student_id(self):
        with self.assertRaises(ValueError):
            self.service.add_student(
                Student(0, "Teja", 22, "Python")
            )

    def test_empty_student_name(self):
        with self.assertRaises(ValueError):
            self.service.add_student(
                Student(1, "", 22, "Python")
            )

    def test_invalid_student_age(self):
        with self.assertRaises(ValueError):
            self.service.add_student(
                Student(1, "Teja", 0, "Python")
            )

    def test_empty_student_course(self):
        with self.assertRaises(ValueError):
            self.service.add_student(
                Student(1, "Teja", 22, "")
            )


if __name__ == "__main__":
    unittest.main()