# PY-ADV-03 - Task 6
# Handling Missing and Incorrect Values


print("=== 1. Original Data ===")

students = [
    {"name": "Teja", "age": 25, "score": 85},
    {"name": "Ajay", "age": None, "score": 78},
    {"name": "Sumanth", "age": 26, "score": None},
    {"name": None, "age": 24, "score": 91},
    {"name": "Priya", "age": "twenty", "score": "invalid"},
]

for student in students:
    print(student)


print("\n=== 2. Handling Missing Names ===")


def clean_name(name):
    if name is None or not isinstance(name, str) or not name.strip():
        return "Unknown"

    return name.strip().title()


for student in students:
    student["name"] = clean_name(student["name"])

print("Names cleaned successfully.")


print("\n=== 3. Handling Missing Ages ===")


def clean_age(age):
    if age is None:
        return 0

    if isinstance(age, bool):
        return 0

    if isinstance(age, int):
        return age

    if isinstance(age, str):
        try:
            return int(age)
        except ValueError:
            return 0

    return 0


for student in students:
    student["age"] = clean_age(student["age"])

print("Ages cleaned successfully.")


print("\n=== 4. Handling Missing or Incorrect Scores ===")


def clean_score(score):
    if score is None:
        return 0

    if isinstance(score, bool):
        return 0

    if isinstance(score, (int, float)):
        if 0 <= score <= 100:
            return score
        return 0

    if isinstance(score, str):
        try:
            converted_score = float(score)

            if 0 <= converted_score <= 100:
                return converted_score

        except ValueError:
            return 0

    return 0


for student in students:
    student["score"] = clean_score(student["score"])

print("Scores cleaned successfully.")


print("\n=== 5. Cleaned Data ===")

for student in students:
    print(student)


print("\n=== 6. Identifying Corrected Records ===")

for student in students:
    if (
        student["name"] == "Unknown"
        or student["age"] == 0
        or student["score"] == 0
    ):
        print("Corrected record:", student)


print("\n=== 7. Data Cleaning Summary ===")

print("Missing names replaced.")
print("Missing or incorrect ages handled.")
print("Missing or incorrect scores handled.")
print("Invalid numeric values converted safely.")
print("Cleaned records produced successfully.")