from app.models.student import Student


class StudentService:
    """Handles student management operations."""

    def __init__(self):
        self.students = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def get_students(self) -> list[Student]:
        return self.students