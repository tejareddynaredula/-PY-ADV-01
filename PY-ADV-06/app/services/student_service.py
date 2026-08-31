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