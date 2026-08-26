# PY-ADV-03 - Task 14
# Reusable Utility Modules

import json
import csv
from datetime import datetime


print("=== 1. Data Validation Utility ===")


def validate_score(score):
    """Validate whether a score is between 0 and 100."""

    if isinstance(score, bool):
        return False

    if not isinstance(score, (int, float)):
        return False

    return 0 <= score <= 100


print("Score 85 valid:", validate_score(85))
print("Score 120 valid:", validate_score(120))
print("Score 'invalid' valid:", validate_score("invalid"))


print("\n=== 2. Grade Calculation Utility ===")


def calculate_grade(score):
    """Calculate grade based on score."""

    if not validate_score(score):
        return "Invalid"

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print("85 ->", calculate_grade(85))
print("91 ->", calculate_grade(91))
print("120 ->", calculate_grade(120))


print("\n=== 3. JSON Utility ===")


def save_json(data, filename):
    """Save Python data to a JSON file."""

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return True


def load_json(filename):
    """Load JSON data from a file."""

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


sample_data = {
    "name": "Teja",
    "course": "Python AI/ML",
    "score": 85
}

save_json(sample_data, "utility_data.json")

loaded_data = load_json("utility_data.json")

print("JSON data saved and loaded successfully.")
print("Loaded data:", loaded_data)


print("\n=== 4. CSV Utility ===")


def save_csv(data, filename):
    """Save a list of dictionaries to CSV."""

    if not data:
        return False

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

    return True


def load_csv(filename):
    """Load CSV data as a list of dictionaries."""

    with open(
        filename,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        return list(reader)


students = [
    {
        "name": "Teja",
        "score": 85
    },
    {
        "name": "Ajay",
        "score": 78
    }
]

save_csv(students, "utility_students.csv")

loaded_students = load_csv("utility_students.csv")

print("CSV data saved and loaded successfully.")
print("Loaded students:", loaded_students)


print("\n=== 5. Date and Time Utility ===")


def get_current_timestamp():
    """Return the current date and time."""

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


timestamp = get_current_timestamp()

print("Current timestamp:", timestamp)


print("\n=== 6. Reusable Processing Utility ===")


def process_student(student):
    """Validate and transform a student record."""

    score = student.get("score")

    if not validate_score(score):
        return None

    return {
        "name": student.get("name", "Unknown"),
        "score": score,
        "grade": calculate_grade(score),
        "processed_at": get_current_timestamp()
    }


student = {
    "name": "Sumanth",
    "score": 91
}

processed_student = process_student(student)

print("Processed student:")
print(processed_student)


print("\n=== 7. Utility Module Summary ===")

print("Validation utility created.")
print("Grade calculation utility created.")
print("JSON utilities created.")
print("CSV utilities created.")
print("Datetime utility created.")
print("Reusable student processing utility created.")