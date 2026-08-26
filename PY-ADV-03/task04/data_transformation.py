# PY-ADV-03 - Task 4
# Data Transformation Functions


print("=== 1. Original Student Data ===")

students = [
    {
        "name": "Teja",
        "age": 25,
        "score": 85,
        "course": "Python AI/ML"
    },
    {
        "name": "Ajay",
        "age": 24,
        "score": 78,
        "course": "Data Science"
    },
    {
        "name": "Sumanth",
        "age": 26,
        "score": 91,
        "course": "Machine Learning"
    }
]

for student in students:
    print(student)


print("\n=== 2. Normalize Student Names ===")


def normalize_name(name):
    return name.strip().title()


for student in students:
    student["name"] = normalize_name(student["name"])

print("Names normalized successfully.")


print("\n=== 3. Calculate Grade ===")


def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


for student in students:
    student["grade"] = calculate_grade(student["score"])

for student in students:
    print(student["name"], "->", student["grade"])


print("\n=== 4. Transform Student Records ===")


def transform_student(student):
    return {
        "student_name": student["name"],
        "course": student["course"],
        "score": student["score"],
        "grade": student["grade"],
        "status": "Pass" if student["score"] >= 60 else "Fail"
    }


transformed_students = [
    transform_student(student)
    for student in students
]

for student in transformed_students:
    print(student)


print("\n=== 5. Filter Passed Students ===")


def filter_passed_students(student_list):
    return [
        student
        for student in student_list
        if student["status"] == "Pass"
    ]


passed_students = filter_passed_students(transformed_students)

for student in passed_students:
    print(student)


print("\n=== 6. Calculate Average Score ===")


def calculate_average_score(student_list):
    if not student_list:
        return 0

    total = sum(student["score"] for student in student_list)
    return total / len(student_list)


average_score = calculate_average_score(transformed_students)

print("Average score:", average_score)


print("\n=== 7. Final Transformed Data ===")

for student in transformed_students:
    print(
        f"{student['student_name']} | "
        f"{student['course']} | "
        f"Score: {student['score']} | "
        f"Grade: {student['grade']} | "
        f"Status: {student['status']}"
    )


print("\n=== 8. Data Transformation Summary ===")

print("Names normalized.")
print("Grades calculated.")
print("Student records transformed.")
print("Passed students filtered.")
print("Average score calculated.")
print("Reusable transformation functions created.")