from app.models.student import Student


def find_student_by_id(
    students: list[Student], student_id: int
) -> Student | None:
    """Find a student by ID."""
    for student in students:
        if student.student_id == student_id:
            return student
    return None


def validate_student_data(
    student_id: int,
    name: str,
    age: int,
    course: str,
) -> None:
    """Validate student information before creation or update."""
    if student_id <= 0:
        raise ValueError("Student ID must be greater than 0.")

    if not name.strip():
        raise ValueError("Student name cannot be empty.")

    if age <= 0:
        raise ValueError("Student age must be greater than 0.")

    if not course.strip():
        raise ValueError("Student course cannot be empty.")