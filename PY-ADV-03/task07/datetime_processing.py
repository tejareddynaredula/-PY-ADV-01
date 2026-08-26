# PY-ADV-03 - Task 7
# Working with Python datetime

from datetime import datetime, date, timedelta


print("=== 1. Current Date and Time ===")

current_datetime = datetime.now()

print("Current date and time:", current_datetime)
print("Current date:", current_datetime.date())
print("Current time:", current_datetime.time())


print("\n=== 2. Creating Specific Dates ===")

project_start = date(2026, 8, 26)
project_end = date(2026, 9, 10)

print("Project start:", project_start)
print("Project end:", project_end)


print("\n=== 3. Date Difference ===")

duration = project_end - project_start

print("Project duration:", duration.days, "days")


print("\n=== 4. Adding and Subtracting Dates ===")

today = date.today()

future_date = today + timedelta(days=7)
past_date = today - timedelta(days=7)

print("Today:", today)
print("Date after 7 days:", future_date)
print("Date before 7 days:", past_date)


print("\n=== 5. Formatting Date and Time ===")

formatted_datetime = current_datetime.strftime(
    "%d-%m-%Y %H:%M:%S"
)

print("Formatted date and time:", formatted_datetime)


print("\n=== 6. Parsing Date String ===")

date_string = "26-08-2026"

parsed_date = datetime.strptime(
    date_string,
    "%d-%m-%Y"
)

print("Original string:", date_string)
print("Parsed date:", parsed_date.date())


print("\n=== 7. Comparing Dates ===")

deadline = date(2026, 9, 1)

if today <= deadline:
    print("The deadline has not passed.")
else:
    print("The deadline has passed.")


print("\n=== 8. Calculating Age ===")


def calculate_age(birth_date):
    today = date.today()

    age = today.year - birth_date.year

    if (today.month, today.day) < (
        birth_date.month,
        birth_date.day
    ):
        age -= 1

    return age


birth_date = date(2001, 5, 15)

age = calculate_age(birth_date)

print("Birth date:", birth_date)
print("Age:", age)


print("\n=== 9. DateTime Difference ===")

start_time = datetime(2026, 8, 26, 9, 0, 0)
end_time = datetime(2026, 8, 26, 17, 30, 0)

time_difference = end_time - start_time

print("Start time:", start_time)
print("End time:", end_time)
print("Time difference:", time_difference)


print("\n=== 10. DateTime Summary ===")

print("Current date and time retrieved.")
print("Specific dates created.")
print("Date differences calculated.")
print("Dates added and subtracted.")
print("Dates formatted successfully.")
print("Date strings parsed successfully.")
print("Dates compared successfully.")
print("Age calculated using datetime.")
print("DateTime differences calculated.")