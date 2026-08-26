# PY-ADV-03 - Task 1
# Read and Write CSV Files

import csv


print("=== 1. Creating CSV File ===")

filename = "students.csv"

students = [
    ["Name", "Age", "Course", "Score"],
    ["Teja", 25, "Python AI/ML", 85],
    ["Ajay", 24, "Data Science", 78],
    ["Sumanth", 26, "Machine Learning", 91],
]

with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created successfully.")


print("\n=== 2. Reading CSV File ===")

with open(filename, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


print("\n=== 3. Reading CSV as Dictionaries ===")

with open(filename, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(
            f"Name: {row['Name']}, "
            f"Course: {row['Course']}, "
            f"Score: {row['Score']}"
        )


print("\n=== 4. Filtering CSV Data ===")

with open(filename, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        score = float(row["Score"])

        if score >= 80:
            print(
                f"{row['Name']} scored {score} "
                f"and passed the filter."
            )


print("\n=== 5. CSV Processing Summary ===")

print("CSV file written successfully.")
print("CSV file read successfully.")
print("CSV data converted into dictionaries.")
print("CSV records filtered successfully.")