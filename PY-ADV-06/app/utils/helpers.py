from app.models.student import Student


def find_student_by_id(
    students: list[Student], student_id: int
) -> Student | None:
    """Find a student by ID."""
    for student in students:
        if student.student_id == student_id:
            return student
    return None