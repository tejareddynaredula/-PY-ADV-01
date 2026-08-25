# PY-ADV-01 - Task 2
# Mutable vs Immutable Objects


print("=== 1. Mutable Object - List ===")

numbers = [1, 2, 3]

print("Before modification:", numbers)
print("ID before modification:", id(numbers))

numbers.append(4)

print("After modification:", numbers)
print("ID after modification:", id(numbers))


print("\n=== 2. Immutable Object - String ===")

name = "Python"

print("Before modification:", name)
print("ID before modification:", id(name))

name = name + " AI"

print("After modification:", name)
print("ID after modification:", id(name))


print("\n=== 3. Mutable Object - Dictionary ===")

student = {
    "name": "Teja",
    "age": 25
}

print("Before modification:", student)
print("ID before modification:", id(student))

student["age"] = 26

print("After modification:", student)
print("ID after modification:", id(student))


print("\n=== 4. Immutable Object - Integer ===")

age = 25

print("Before modification:", age)
print("ID before modification:", id(age))

age = 26

print("After modification:", age)
print("ID after modification:", id(age))