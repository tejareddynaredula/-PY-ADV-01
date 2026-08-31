from app.exceptions.student_exceptions import StudentNotFoundError
from app.models.student import Student


class StudentService:
    """Handles student management operations."""

    def __init__(self):
        self.students = []

    def add_student(self, student: Student) -> None:
        """Add a student to the student list."""
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
        for student in self.students:
            if student.student_id == student_id:
                student.name = name
                student.age = age
                student.course = course
                return

        raise StudentNotFoundError(
            f"Student with ID {student_id} was not found."
        )