# PY-ADV-01 - Task 10
# Python Comprehensions


print("=== 1. Basic List Comprehension ===")

numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print("Numbers:", numbers)
print("Squares:", squares)


print("\n=== 2. List Comprehension with Condition ===")

even_numbers = [number for number in numbers if number % 2 == 0]

print("Even numbers:", even_numbers)


print("\n=== 3. List Comprehension with Transformation ===")

names = ["teja", "ajay", "python", "developer"]

uppercase_names = [name.upper() for name in names]

print("Original:", names)
print("Uppercase:", uppercase_names)


print("\n=== 4. Conditional Expression in Comprehension ===")

labels = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print("Numbers:", numbers)
print("Labels:", labels)


print("\n=== 5. Nested List Comprehension ===")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [
    value
    for row in matrix
    for value in row
]

print("Matrix:", matrix)
print("Flattened:", flattened)


print("\n=== 6. Dictionary Comprehension ===")

number_dictionary = {
    number: number * number
    for number in numbers
}

print("Dictionary:", number_dictionary)


print("\n=== 7. Dictionary Comprehension with Condition ===")

even_dictionary = {
    number: number * number
    for number in numbers
    if number % 2 == 0
}

print("Even number dictionary:", even_dictionary)


print("\n=== 8. Set Comprehension ===")

values = [1, 2, 2, 3, 3, 4, 5, 5]

unique_squares = {
    number * number
    for number in values
}

print("Original values:", values)
print("Unique squares:", unique_squares)


print("\n=== 9. Generator Expression ===")

generator = (
    number * number
    for number in range(1, 6)
)

print("Generator type:", type(generator))

print("Generated values:")

for value in generator:
    print(value)


print("\n=== 10. Practical Data Processing ===")

students = [
    {"name": "Teja", "marks": 85},
    {"name": "Ajay", "marks": 72},
    {"name": "Rahul", "marks": 91},
    {"name": "Priya", "marks": 65}
]

passed_students = [
    student["name"]
    for student in students
    if student["marks"] >= 70
]

print("Passed students:", passed_students)


student_scores = {
    student["name"]: student["marks"]
    for student in students
}

print("Student scores:", student_scores)


print("\n=== 11. Edge Cases ===")

empty_list = []

empty_result = [
    number * 2
    for number in empty_list
]

print("Empty input:", empty_list)
print("Result:", empty_result)


negative_numbers = [-3, -2, -1, 0, 1, 2, 3]

positive_numbers = [
    number
    for number in negative_numbers
    if number > 0
]

print("Positive numbers:", positive_numbers)


duplicate_values = [1, 1, 2, 2, 3, 3]

unique_values = {
    number
    for number in duplicate_values
}

print("Unique values:", unique_values)
print("\n=== 12. Handling Mixed Data ===")

mixed_values = [1, 2, "3", 4, "5"]

numeric_values = [
    value
    for value in mixed_values
    if isinstance(value, (int, float))
]

print("Mixed input:", mixed_values)
print("Numeric values only:", numeric_values)