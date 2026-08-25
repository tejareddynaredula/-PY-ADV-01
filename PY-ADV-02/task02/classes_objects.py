# PY-ADV-02 - Task 2
# Classes and Objects


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

    def update_course(self, new_course):
        self.course = new_course
        print("Course updated to:", self.course)


print("=== 1. Creating Objects ===")

student1 = Student("Teja", 25, "Python AI/ML")
student2 = Student("Sumanth", 24, "Django")

print("Student objects created successfully.")


print("\n=== 2. Student 1 Details ===")

student1.display_details()


print("\n=== 3. Student 2 Details ===")

student2.display_details()


print("\n=== 4. Accessing Object Attributes ===")

print("Student 1 Name:", student1.name)
print("Student 1 Course:", student1.course)


print("\n=== 5. Updating Object Data ===")

student1.update_course("Advanced Python")


print("\n=== 6. Independent Objects ===")

student1.age = 26

print("Student 1 Age:", student1.age)
print("Student 2 Age:", student2.age)


print("\n=== 7. Object Types ===")

print("Type of student1:", type(student1))
print("Type of student2:", type(student2))


print("\n=== 8. Multiple Objects ===")

students = [
    Student("Rahul", 23, "Machine Learning"),
    Student("Priya", 22, "Data Science"),
    Student("Ajay", 24, "Django")
]

for student in students:
    print("\nStudent:")
    student.display_details()