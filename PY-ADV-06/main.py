from app.models.student import Student
from app.services.student_service import StudentService


def main() -> None:
    """Run the Student Management System."""
    service = StudentService()

    student = Student(1, "Teja", 22, "Python")
    service.add_student(student)

    print("Student Management System")

    for student in service.get_students():
        print(
            f"ID: {student.student_id}, "
            f"Name: {student.name}, "
            f"Age: {student.age}, "
            f"Course: {student.course}"
        )


if __name__ == "__main__":
    main()