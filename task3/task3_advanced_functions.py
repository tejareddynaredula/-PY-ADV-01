# PY-ADV-01 - Task 3
# Advanced Functions


print("=== 1. Default Arguments ===")


def greet(name, message="Welcome"):
    return f"{message}, {name}!"


print(greet("Teja"))
print(greet("Teja", "Good Morning"))


print("\n=== 2. Keyword Arguments ===")


def student_details(name, age, course):
    return f"Name: {name}, Age: {age}, Course: {course}"


print(student_details(
    name="Teja",
    age=25,
    course="Python AI/ML"
))


print("\n=== 3. Returning Multiple Values ===")


def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


result = calculate(10, 5)

print("Addition:", result[0])
print("Subtraction:", result[1])
print("Multiplication:", result[2])


print("\n=== 4. Function Returning a Function ===")


def create_multiplier(number):

    def multiplier(value):
        return value * number

    return multiplier


double = create_multiplier(2)
triple = create_multiplier(3)

print("Double of 10:", double(10))
print("Triple of 10:", triple(10))


print("\n=== 5. Function as an Argument ===")


def apply_operation(a, b, operation):
    return operation(a, b)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


print("Addition:", apply_operation(10, 5, add))
print("Multiplication:", apply_operation(10, 5, multiply))