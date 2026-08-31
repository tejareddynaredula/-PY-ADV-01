import unittest

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


if __name__ == "__main__":
    unittest.main()