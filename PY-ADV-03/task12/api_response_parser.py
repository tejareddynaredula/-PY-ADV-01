# PY-ADV-03 - Task 12
# Parse API Responses

import json


print("=== 1. Sample API Response ===")

api_response = {
    "status": "success",
    "data": {
        "id": 101,
        "name": "Teja",
        "course": "Python AI/ML",
        "score": 85
    }
}

print(json.dumps(api_response, indent=4))


print("\n=== 2. Parse API Response ===")


def parse_api_response(response):
    if not isinstance(response, dict):
        print("Error: API response must be a dictionary.")
        return None

    if response.get("status") != "success":
        print("Error: API request was not successful.")
        return None

    data = response.get("data")

    if not isinstance(data, dict):
        print("Error: Invalid data section.")
        return None

    return data


student = parse_api_response(api_response)

print("Parsed data:", student)


print("\n=== 3. Extract Required Fields ===")


def extract_student_details(data):
    if not data:
        return None

    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "course": data.get("course"),
        "score": data.get("score")
    }


student_details = extract_student_details(student)

print("Student ID:", student_details["id"])
print("Name:", student_details["name"])
print("Course:", student_details["course"])
print("Score:", student_details["score"])


print("\n=== 4. Parse JSON String ===")


json_response = """
{
    "status": "success",
    "data": {
        "id": 102,
        "name": "Ajay",
        "course": "Data Science",
        "score": 78
    }
}
"""


def parse_json_string(json_text):
    try:
        return json.loads(json_text)

    except json.JSONDecodeError:
        print("Error: Invalid JSON response.")
        return None


parsed_json = parse_json_string(json_response)

print("JSON parsed successfully.")

parsed_student = parse_api_response(parsed_json)

print("Parsed student:", parsed_student)


print("\n=== 5. Handling Missing Fields ===")


incomplete_response = {
    "status": "success",
    "data": {
        "id": 103,
        "name": "Sumanth"
    }
}

incomplete_student = parse_api_response(incomplete_response)

print("Name:", incomplete_student.get("name"))
print("Course:", incomplete_student.get("course", "Not Available"))
print("Score:", incomplete_student.get("score", "Not Available"))


print("\n=== 6. Handling Failed API Response ===")


failed_response = {
    "status": "error",
    "message": "Student data could not be retrieved."
}

failed_data = parse_api_response(failed_response)

print("Parsed result:", failed_data)


print("\n=== 7. API Response Parsing Summary ===")

print("API response structure validated.")
print("JSON response parsed successfully.")
print("Required fields extracted.")
print("Missing fields handled safely.")
print("Failed API responses handled.")
print("Reusable API response parser created.")