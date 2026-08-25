# PY-ADV-01 - Task 14
# Code Refactoring and Improvement


print("=== 1. Original vs Refactored Logic ===")


# Original approach
numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

print("Original total:", total)


# Refactored approach
def calculate_total(values):
    return sum(values)


refactored_total = calculate_total(numbers)

print("Refactored total:", refactored_total)


print("\n=== 2. Removing Duplicate Logic ===")


def calculate_square(number):
    return number * number


def calculate_cube(number):
    return number * number * number


number = 5

print("Square:", calculate_square(number))
print("Cube:", calculate_cube(number))


print("\n=== 3. Reusable Validation Function ===")


def is_valid_score(score):
    return isinstance(score, (int, float)) and 0 <= score <= 100


scores = [85, 72, 105, -10, 91]

for score in scores:
    if is_valid_score(score):
        print("Valid score:", score)
    else:
        print("Invalid score:", score)


print("\n=== 4. Refactoring Data Processing ===")


students = [
    {"name": "Teja", "score": 85},
    {"name": "Ajay", "score": 72},
    {"name": "Rahul", "score": 91},
    {"name": "Priya", "score": 65}
]


def get_passed_students(student_list, passing_score=70):
    return [
        student["name"]
        for student in student_list
        if student["score"] >= passing_score
    ]


passed_students = get_passed_students(students)

print("Passed students:", passed_students)


print("\n=== 5. Separating Processing from Output ===")


def calculate_average(values):
    if not values:
        return 0

    return sum(values) / len(values)


def display_average(values):
    average = calculate_average(values)
    print("Average:", average)


marks = [80, 70, 90, 60]

display_average(marks)


print("\n=== 6. Improving Variable Names ===")


student_scores = [85, 90, 78, 92]

total_score = sum(student_scores)
number_of_students = len(student_scores)

average_score = total_score / number_of_students

print("Student scores:", student_scores)
print("Total score:", total_score)
print("Number of students:", number_of_students)
print("Average score:", average_score)


print("\n=== 7. Error Handling in Refactored Code ===")


def safe_divide(first_number, second_number):
    try:
        return first_number / second_number
    except ZeroDivisionError:
        return None


result1 = safe_divide(10, 2)
result2 = safe_divide(10, 0)

print("10 / 2:", result1)
print("10 / 0:", result2)


print("\n=== 8. Refactored Dictionary Processing ===")


employees = [
    {"name": "Teja", "salary": 50000},
    {"name": "Ajay", "salary": 65000},
    {"name": "Rahul", "salary": 45000}
]


def find_highest_paid_employee(employee_list):
    if not employee_list:
        return None

    return max(
        employee_list,
        key=lambda employee: employee["salary"]
    )


highest_paid = find_highest_paid_employee(employees)

print("Highest paid employee:", highest_paid)


print("\n=== 9. Handling Empty Input ===")


def find_largest(values):
    if not values:
        return None

    return max(values)


print("Largest:", find_largest([10, 25, 7, 42]))
print("Largest from empty list:", find_largest([]))


print("\n=== 10. Final Refactored Workflow ===")


def process_student_scores(student_list):
    if not student_list:
        return {
            "count": 0,
            "average": 0,
            "passed": []
        }

    valid_students = [
        student
        for student in student_list
        if is_valid_score(student.get("score"))
    ]

    if not valid_students:
        return {
            "count": 0,
            "average": 0,
            "passed": []
        }

    scores = [
        student["score"]
        for student in valid_students
    ]

    passed_students = [
        student["name"]
        for student in valid_students
        if student["score"] >= 70
    ]

    return {
        "count": len(valid_students),
        "average": calculate_average(scores),
        "passed": passed_students
    }


student_data = [
    {"name": "Teja", "score": 85},
    {"name": "Ajay", "score": 72},
    {"name": "Rahul", "score": 91},
    {"name": "Priya", "score": 65},
    {"name": "Invalid Student", "score": 120}
]


result = process_student_scores(student_data)

print("Valid student count:", result["count"])
print("Average score:", result["average"])
print("Passed students:", result["passed"])


print("\n=== 11. Refactoring Edge Cases ===")


print("Empty student data:", process_student_scores([]))

invalid_student_data = [
    {"name": "Student A", "score": 150},
    {"name": "Student B", "score": -20}
]

print(
    "Only invalid student data:",
    process_student_scores(invalid_student_data)
)


print("\n=== 12. Refactoring Summary ===")

print("Code duplication reduced.")
print("Reusable functions created.")
print("Validation added.")
print("Error handling added.")
print("Variable names improved.")
print("Processing separated from output.")
print("Edge cases handled.")
print("Code readability improved.")