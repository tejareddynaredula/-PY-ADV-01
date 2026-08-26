# PY-ADV-03 - Task 13
# Store Processed Results Locally

import json
import csv


print("=== 1. Processed Data ===")

processed_students = [
    {
        "id": 101,
        "name": "Teja",
        "course": "Python AI/ML",
        "score": 85,
        "grade": "B",
        "status": "Pass"
    },
    {
        "id": 102,
        "name": "Ajay",
        "course": "Data Science",
        "score": 78,
        "grade": "C",
        "status": "Pass"
    },
    {
        "id": 103,
        "name": "Sumanth",
        "course": "Machine Learning",
        "score": 91,
        "grade": "A",
        "status": "Pass"
    }
]

for student in processed_students:
    print(student)


print("\n=== 2. Storing Results as JSON ===")


def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"JSON data saved to {filename}")


save_to_json(
    processed_students,
    "processed_students.json"
)


print("\n=== 3. Reading Results from JSON ===")


def read_from_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


json_data = read_from_json("processed_students.json")

for student in json_data:
    print(student)


print("\n=== 4. Storing Results as CSV ===")


def save_to_csv(data, filename):
    if not data:
        print("No data available for CSV storage.")
        return

    fieldnames = data[0].keys()

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(data)

    print(f"CSV data saved to {filename}")


save_to_csv(
    processed_students,
    "processed_students.csv"
)


print("\n=== 5. Reading Results from CSV ===")


def read_from_csv(filename):
    with open(
        filename,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        return list(reader)


csv_data = read_from_csv("processed_students.csv")

for student in csv_data:
    print(student)


print("\n=== 6. Storage Verification ===")

print("JSON records:", len(json_data))
print("CSV records:", len(csv_data))

if len(json_data) == len(processed_students):
    print("JSON storage verified successfully.")

if len(csv_data) == len(processed_students):
    print("CSV storage verified successfully.")


print("\n=== 7. Local Storage Summary ===")

print("Processed data stored as JSON.")
print("Processed data stored as CSV.")
print("JSON data read successfully.")
print("CSV data read successfully.")
print("Stored records verified successfully.")