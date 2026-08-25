# PY-ADV-01 - Task 1
# Python Execution Flow and Object Model


print("=== 1. Python Execution Flow ===")

print("Step 1")
print("Step 2")
print("Step 3")


print("\n=== 2. Python Objects ===")

name = "Teja"
age = 25
marks = 85.5

print("Name:", name)
print("Age:", age)
print("Marks:", marks)


print("\n=== 3. Object Type ===")

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of marks:", type(marks))


print("\n=== 4. Object Identity ===")

a = 100
b = a

print("Value of a:", a)
print("Value of b:", b)

print("ID of a:", id(a))
print("ID of b:", id(b))

print("Are a and b the same object?", a is b)


print("\n=== 5. Different Objects ===")

x = [1, 2, 3]
y = [1, 2, 3]

print("x:", x)
print("y:", y)

print("ID of x:", id(x))
print("ID of y:", id(y))

print("Are x and y the same object?", x is y)
print("Do x and y have the same value?", x == y)



print("=== 4. Object Identity ===")

a = 100
b = a

print("Value of a:", a)
print("Value of b:", b)

print("ID of a:", id(a))
print("ID of b:", id(b))

print("Are a and b the same object?", a is b)