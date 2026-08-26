# PY-ADV-03 - Task 3
# Working with Nested JSON

import json


print("=== 1. Creating Nested JSON Data ===")

company = {
    "name": "Tech Solutions",
    "location": {
        "city": "Hyderabad",
        "country": "India"
    },
    "employees": [
        {
            "id": "EMP001",
            "name": "Teja",
            "role": "Python Developer",
            "skills": ["Python", "Django", "SQL"]
        },
        {
            "id": "EMP002",
            "name": "Ajay",
            "role": "Data Scientist",
            "skills": ["Python", "Machine Learning", "Pandas"]
        }
    ]
}

print(json.dumps(company, indent=4))


print("\n=== 2. Accessing Nested Values ===")

print("Company:", company["name"])
print("City:", company["location"]["city"])
print("Country:", company["location"]["country"])


print("\n=== 3. Processing Nested Employees ===")

for employee in company["employees"]:
    print("Employee ID:", employee["id"])
    print("Name:", employee["name"])
    print("Role:", employee["role"])
    print("Skills:", ", ".join(employee["skills"]))
    print()


print("=== 4. Accessing a Specific Nested Employee ===")

first_employee = company["employees"][0]

print("Name:", first_employee["name"])
print("Role:", first_employee["role"])
print("First Skill:", first_employee["skills"][0])


print("\n=== 5. Updating Nested JSON ===")

company["location"]["city"] = "Bengaluru"
company["employees"][0]["role"] = "Senior Python Developer"
company["employees"][1]["skills"].append("NumPy")

print("Updated City:", company["location"]["city"])
print("Updated Role:", company["employees"][0]["role"])
print("Updated Skills:", company["employees"][1]["skills"])


print("\n=== 6. Converting Nested JSON to String ===")

json_string = json.dumps(company, indent=4)

print(json_string)


print("\n=== 7. Nested JSON Summary ===")

print("Nested objects accessed successfully.")
print("Nested lists processed successfully.")
print("Nested values updated successfully.")
print("Nested JSON converted to a JSON string successfully.")