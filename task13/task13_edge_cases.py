# PY-ADV-01 - Task 13
# Edge Cases and Invalid Input Handling


print("=== 1. Empty Input ===")

text = ""

if not text:
    print("Input is empty.")
else:
    print("Input:", text)


print("\n=== 2. Invalid Number Input ===")

user_input = "abc"

try:
    number = int(user_input)
    print("Number:", number)
except ValueError:
    print("Invalid number input. Please enter a valid integer.")


print("\n=== 3. Division by Zero ===")

number = 10
divisor = 0

try:
    result = number / divisor
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")


print("\n=== 4. Negative Value Handling ===")

age = -5

if age < 0:
    print("Invalid age: age cannot be negative.")
else:
    print("Age:", age)


print("\n=== 5. Invalid List Values ===")

values = [10, 20, "abc", 30, "xyz", 40]

numeric_values = []

for value in values:
    if isinstance(value, (int, float)):
        numeric_values.append(value)
    else:
        print("Ignoring invalid value:", value)

print("Valid numeric values:", numeric_values)


print("\n=== 6. Missing Dictionary Key ===")

student = {
    "name": "Teja",
    "age": 25
}

try:
    course = student["course"]
    print("Course:", course)
except KeyError:
    print("Course information is not available.")


print("\n=== 7. Invalid Menu Choice ===")

menu_choice = 5

valid_choices = [1, 2, 3]

if menu_choice in valid_choices:
    print("Valid menu choice:", menu_choice)
else:
    print("Invalid menu choice.")


print("\n=== 8. File Not Found Handling ===")

filename = "missing_file.txt"

try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found:", filename)


print("\n=== 9. None Input ===")

value = None

if value is None:
    print("No value was provided.")
else:
    print("Value:", value)


print("\n=== 10. Mixed Data Handling ===")

mixed_values = [10, "20", 30, None, "abc", 40]

valid_numbers = []

for value in mixed_values:
    if isinstance(value, (int, float)):
        valid_numbers.append(value)

print("Mixed values:", mixed_values)
print("Valid numbers:", valid_numbers)


print("\n=== 11. Boundary Values ===")

number = 0

if number == 0:
    print("Value is exactly zero.")

number = 100

if number >= 100:
    print("Value reached the upper boundary:", number)


print("\n=== 12. Empty List Handling ===")

numbers = []

if not numbers:
    print("List is empty.")
else:
    print("Largest value:", max(numbers))


print("\n=== 13. Safe List Access ===")

numbers = [10, 20, 30]
index = 5

try:
    print("Value:", numbers[index])
except IndexError:
    print("Invalid index. The requested position does not exist.")


print("\n=== 14. String Conversion Handling ===")

values = ["10", "20", "abc", "30"]

converted_values = []

for value in values:
    try:
        converted_values.append(int(value))
    except ValueError:
        print("Cannot convert to integer:", value)

print("Converted values:", converted_values)


print("\n=== 15. Final Validation Example ===")

score = 105

if score < 0 or score > 100:
    print("Invalid score. Score must be between 0 and 100.")
else:
    print("Valid score:", score)