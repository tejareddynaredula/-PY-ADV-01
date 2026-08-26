# PY-ADV-03 - Task 5
# Validate Incoming Data


print("=== 1. Validating Student Data ===")


def validate_student(student):
    errors = []

    if not isinstance(student, dict):
        return ["Student data must be a dictionary."]

    name = student.get("name")
    age = student.get("age")
    course = student.get("course")
    score = student.get("score")

    if not isinstance(name, str) or not name.strip():
        errors.append("Name must be a non-empty string.")

    if not isinstance(age, int) or isinstance(age, bool):
        errors.append("Age must be an integer.")
    elif age < 18 or age > 100:
        errors.append("Age must be between 18 and 100.")

    if not isinstance(course, str) or not course.strip():
        errors.append("Course must be a non-empty string.")

    if not isinstance(score, (int, float)) or isinstance(score, bool):
        errors.append("Score must be a number.")
    elif score < 0 or score > 100:
        errors.append("Score must be between 0 and 100.")

    return errors


students = [
    {
        "name": "Teja",
        "age": 25,
        "course": "Python AI/ML",
        "score": 85
    },
    {
        "name": "Ajay",
        "age": 24,
        "course": "Data Science",
        "score": 78
    },
    {
        "name": "Invalid Student",
        "age": 15,
        "course": "",
        "score": 120
    }
]


for student in students:
    errors = validate_student(student)

    if errors:
        print("\nInvalid student:")
        print(student)

        for error in errors:
            print("Error:", error)
    else:
        print("\nValid student:")
        print(student)


print("\n=== 2. Validating Individual Records ===")


test_records = [
    {
        "name": "Rahul",
        "age": 30,
        "course": "Python",
        "score": 90
    },
    {
        "name": "",
        "age": 25,
        "course": "Python",
        "score": 80
    },
    {
        "name": "Priya",
        "age": 17,
        "course": "Data Science",
        "score": 75
    },
    {
        "name": "Kiran",
        "age": 28,
        "course": "Machine Learning",
        "score": 105
    }
]


for record in test_records:
    errors = validate_student(record)

    if errors:
        print("Validation failed for:", record["name"] or "Unnamed")
        for error in errors:
            print(" -", error)
    else:
        print("Validation passed for:", record["name"])


print("\n=== 3. Validation Summary ===")

print("Required fields checked.")
print("Data types checked.")
print("Age range checked.")
print("Score range checked.")
print("Empty values checked.")
print("Reusable validation function created.")