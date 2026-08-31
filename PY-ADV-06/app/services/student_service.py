from app.exceptions.student_exceptions import StudentNotFoundError
from app.models.student import Student
from app.utils.helpers import validate_student_data
from app.utils.logger import get_logger


class StudentService:
    """Handles student management operations."""

    def __init__(self):
        self.students = []
        self.logger = get_logger(__name__)

    def add_student(self, student: Student) -> None:
        """Add a student to the student list."""
        validate_student_data(
            student.student_id,
            student.name,
            student.age,
            student.course,
        )
        self.students.append(student)
        self.logger.info("Student %s added successfully.", student.student_id)

    def get_students(self) -> list[Student]:
        """Return all students."""
        return self.students

    def find_student(self, student_id: int) -> Student:
        """Find a student by ID."""
        for student in self.students:
            if student.student_id == student_id:
                self.logger.info(
                    "Student %s found successfully.", student_id
                )
                return student

        self.logger.error("Student %s not found.", student_id)
        raise StudentNotFoundError(
            f"Student with ID {student_id} was not found."
        )

    def update_student(
        self,
        student_id: int,
        name: str,
        age: int,
        course: str,
    ) -> None:
        """Update an existing student's details."""
        validate_student_data(student_id, name, age, course)

        for student in self.students:
            if student.student_id == student_id:
                student.name = name
                student.age = age
                student.course = course
                self.logger.info(
                    "Student %s updated successfully.", student_id
                )
                return

        self.logger.error("Student %s not found for update.", student_id)
        raise StudentNotFoundError(
            f"Student with ID {student_id} was not found."
        )

    def delete_student(self, student_id: int) -> None:
        """Delete a student by ID."""
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.logger.info(
                    "Student %s deleted successfully.", student_id
                )
                return

        self.logger.error("Student %s not found for deletion.", student_id)
        raise StudentNotFoundError(
            f"Student with ID {student_id} was not found."
        )