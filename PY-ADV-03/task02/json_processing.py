# PY-ADV-03 - Task 2
# Process JSON Data

import json


print("=== 1. Creating JSON Data ===")

student = {
    "name": "Teja",
    "age": 25,
    "course": "Python AI/ML",
    "score": 85
}

json_data = json.dumps(student, indent=4)

print(json_data)


print("\n=== 2. Writing JSON to File ===")

filename = "student.json"

with open(filename, "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully.")


print("\n=== 3. Reading JSON from File ===")

with open(filename, "r", encoding="utf-8") as file:
    loaded_student = json.load(file)

print("Student data:")
print(loaded_student)


print("\n=== 4. Accessing JSON Values ===")

print("Name:", loaded_student["name"])
print("Age:", loaded_student["age"])
print("Course:", loaded_student["course"])
print("Score:", loaded_student["score"])


print("\n=== 5. Updating JSON Data ===")

loaded_student["score"] = 90

print("Updated score:", loaded_student["score"])


print("\n=== 6. Converting JSON String Back to Python ===")

json_string = '{"name": "Ajay", "age": 24, "course": "Data Science"}'

converted_data = json.loads(json_string)

print("Name:", converted_data["name"])
print("Age:", converted_data["age"])
print("Course:", converted_data["course"])


print("\n=== 7. JSON Processing Summary ===")

print("Python dictionary converted to JSON.")
print("JSON data written to a file.")
print("JSON data read from a file.")
print("JSON values accessed and updated.")
print("JSON string converted back to Python data.")