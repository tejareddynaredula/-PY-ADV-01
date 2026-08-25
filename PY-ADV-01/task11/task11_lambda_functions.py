# PY-ADV-01 - Task 11
# Lambda Functions


print("=== 1. Basic Lambda Function ===")

square = lambda number: number * number

print("Square of 5:", square(5))


print("\n=== 2. Lambda with Multiple Arguments ===")

add = lambda a, b: a + b
multiply = lambda a, b: a * b

print("Addition:", add(10, 20))
print("Multiplication:", multiply(10, 20))


print("\n=== 3. Lambda with map() ===")

numbers = [1, 2, 3, 4, 5]

squares = list(
    map(lambda number: number * number, numbers)
)

print("Numbers:", numbers)
print("Squares:", squares)


print("\n=== 4. Lambda with filter() ===")

even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print("Even numbers:", even_numbers)


print("\n=== 5. Lambda with sorted() ===")

students = [
    ("Teja", 85),
    ("Ajay", 72),
    ("Rahul", 91),
    ("Priya", 65)
]

students_by_marks = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print("Students sorted by marks:")
for student in students_by_marks:
    print(student)


print("\n=== 6. Lambda with Dictionary Data ===")

employees = [
    {"name": "Teja", "salary": 50000},
    {"name": "Ajay", "salary": 65000},
    {"name": "Rahul", "salary": 45000}
]

highest_salary = max(
    employees,
    key=lambda employee: employee["salary"]
)

print("Highest salary employee:", highest_salary)


print("\n=== 7. Lambda with Conditional Expression ===")

check_number = lambda number: (
    "Positive" if number > 0
    else "Negative" if number < 0
    else "Zero"
)

print("10:", check_number(10))
print("-5:", check_number(-5))
print("0:", check_number(0))


print("\n=== 8. Practical Data Processing ===")

prices = [100, 250, 500, 750]

discounted_prices = list(
    map(lambda price: price * 0.90, prices)
)

print("Original prices:", prices)
print("Prices after 10% discount:", discounted_prices)


print("\n=== 9. Lambda with filter() - Practical Example ===")

products = [
    {"name": "Laptop", "price": 70000},
    {"name": "Mouse", "price": 1000},
    {"name": "Keyboard", "price": 2500},
    {"name": "Monitor", "price": 15000}
]

expensive_products = list(
    filter(
        lambda product: product["price"] > 10000,
        products
    )
)

print("Products above 10000:")
for product in expensive_products:
    print(product)


print("\n=== 10. Edge Cases ===")

empty_numbers = []

empty_result = list(
    map(lambda number: number * 2, empty_numbers)
)

print("Empty input:", empty_numbers)
print("Result:", empty_result)


single_number = [10]

single_result = list(
    map(lambda number: number * 2, single_number)
)

print("Single value:", single_number)
print("Result:", single_result)


print("\n=== 11. Handling Mixed Data ===")

mixed_values = [1, 2, "3", 4, "5", 6]

numeric_values = list(
    filter(
        lambda value: isinstance(value, (int, float)),
        mixed_values
    )
)

print("Mixed values:", mixed_values)
print("Numeric values:", numeric_values)