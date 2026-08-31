from app.exceptions.student_exceptions import StudentNotFoundError
from app.models.student import Student
from app.utils.helpers import validate_student_data


class StudentService:
    """Handles student management operations."""

    def __init__(self):
        self.students = []

    def add_student(self, student: Student) -> None:
        """Add a student to the student list."""
        validate_student_data(
            student.student_id,
            student.name,
            student.age,
            student.course,
        )
        self.students.append(student)

    def get_students(self) -> list[Student]:
        """Return all students."""
        return self.students

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
                return

        raise StudentNotFoundError(
            f"Student with ID {student_id} was not found."
        )

    def delete_student(self, student_id: int) -> None:
        """Delete a student by ID."""
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return

        raise StudentNotFoundError(
            f"Student with ID {student_id} was not found."
        )