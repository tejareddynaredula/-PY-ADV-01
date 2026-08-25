# PY-ADV-02 - Task 1
# OOP-Based Student Management Application


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


def main():
    print("=== Student Management System ===")

    student1 = Student("Teja", 25, "Python AI/ML")
    student2 = Student("Sumanth", 24, "Django")

    print("\n--- Student 1 ---")
    student1.display_details()

    print("\n--- Student 2 ---")
    student2.display_details()


if __name__ == "__main__":
    main()