# PY-ADV-02 - Task 3
# Inheritance


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_student_details(self):
        self.display_person_details()
        print("Course:", self.course)


class GraduateStudent(Student):
    def __init__(self, name, age, course, research_topic):
        super().__init__(name, age, course)
        self.research_topic = research_topic

    def display_graduate_details(self):
        self.display_student_details()
        print("Research Topic:", self.research_topic)


print("=== 1. Base Class ===")

person = Person("Ravi", 30)
person.display_person_details()


print("\n=== 2. Student Inheritance ===")

student = Student("Teja", 25, "Python AI/ML")
student.display_student_details()


print("\n=== 3. Graduate Student Inheritance ===")

graduate = GraduateStudent(
    "Sumanth",
    24,
    "Machine Learning",
    "Natural Language Processing"
)

graduate.display_graduate_details()


print("\n=== 4. Inherited Attributes ===")

print("Graduate Student Name:", graduate.name)
print("Graduate Student Age:", graduate.age)
print("Graduate Student Course:", graduate.course)
print("Research Topic:", graduate.research_topic)


print("\n=== 5. Inheritance Relationships ===")

print("Student is a Person:", isinstance(student, Person))
print("GraduateStudent is a Student:", isinstance(graduate, Student))
print("GraduateStudent is a Person:", isinstance(graduate, Person))