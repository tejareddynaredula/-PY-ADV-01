# PY-ADV-03 - Task 8
# Implementing Logging

import logging


print("=== 1. Configuring Logging ===")

logging.basicConfig(
    filename="application.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

print("Logging configured successfully.")


print("\n=== 2. Logging Different Levels ===")

logger.debug("Debug message: application started.")
logger.info("Info message: processing has started.")
logger.warning("Warning message: sample warning detected.")
logger.error("Error message: sample error detected.")

print("DEBUG, INFO, WARNING and ERROR messages logged.")


print("\n=== 3. Logging Data Processing ===")


def process_student(student):
    logger.info("Processing student: %s", student["name"])

    if student["score"] < 0 or student["score"] > 100:
        logger.error(
            "Invalid score %s for student %s",
            student["score"],
            student["name"]
        )
        return False

    logger.info(
        "Student %s processed successfully.",
        student["name"]
    )

    return True


students = [
    {"name": "Teja", "score": 85},
    {"name": "Ajay", "score": 78},
    {"name": "Invalid Student", "score": 120}
]


for student in students:
    result = process_student(student)

    if result:
        print(
            f"{student['name']}: Processing successful."
        )
    else:
        print(
            f"{student['name']}: Processing failed."
        )


print("\n=== 4. Exception Logging ===")


def divide_numbers(first_number, second_number):
    try:
        result = first_number / second_number

        logger.info(
            "Division successful: %s / %s",
            first_number,
            second_number
        )

        return result

    except ZeroDivisionError:
        logger.exception(
            "Division failed because denominator was zero."
        )

        return None


result1 = divide_numbers(10, 2)
result2 = divide_numbers(10, 0)

print("10 / 2:", result1)
print("10 / 0:", result2)


print("\n=== 5. Logging Summary ===")

logger.info("Application processing completed.")

print("Logging levels demonstrated.")
print("Data processing events logged.")
print("Errors logged.")
print("Exceptions logged with details.")
print("Application completed successfully.")