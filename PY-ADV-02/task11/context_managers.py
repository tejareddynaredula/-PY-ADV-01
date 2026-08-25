# PY-ADV-02 - Task 11
# Context Managers


print("=== 1. Basic Context Manager ===")

filename = "student_data.txt"

with open(filename, "w") as file:
    file.write("Name: Teja\n")
    file.write("Course: Python AI/ML\n")
    file.write("Score: 85\n")

print("File created successfully.")


print("\n=== 2. Reading File Using Context Manager ===")

with open(filename, "r") as file:
    content = file.read()

print("File Content:")
print(content)


print("=== 3. Writing Multiple Records ===")

students = [
    "Teja - Python AI/ML",
    "Sumanth - Machine Learning",
    "Ajay - Data Science"
]

with open(filename, "w") as file:
    for student in students:
        file.write(student + "\n")

print("Student records written successfully.")


print("\n=== 4. Reading Updated Records ===")

with open(filename, "r") as file:
    records = file.readlines()

for record in records:
    print(record.strip())


print("\n=== 5. Automatic Resource Management ===")

with open(filename, "r") as file:
    print("File is open inside the with block:", not file.closed)

print("File is open after the with block:", not file.closed)


print("\n=== 6. Context Manager Summary ===")

print("with -> Creates a context for resource management.")
print("open() -> Opens the file.")
print("with block -> Performs file operations safely.")
print("Context exit -> Automatically closes the file.")