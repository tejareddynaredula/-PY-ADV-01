def find_student_by_id(students: list, student_id: int):
    """Find a student by ID."""
    for student in students:
        if student.student_id == student_id:
            return student
    return None