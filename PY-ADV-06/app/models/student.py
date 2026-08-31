class Student:
    """Represents a student."""

    def __init__(self, student_id: int, name: str, age: int, course: str):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course