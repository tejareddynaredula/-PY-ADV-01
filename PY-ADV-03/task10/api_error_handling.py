# PY-ADV-03 - Task 10
# Handle API Errors

import json


print("=== 1. Successful API Response ===")


def handle_api_response(status_code, response_data):
    if status_code == 200:
        print("API request successful.")
        return response_data

    if status_code == 400:
        print("Error 400: Bad Request.")

    elif status_code == 401:
        print("Error 401: Unauthorized.")

    elif status_code == 403:
        print("Error 403: Forbidden.")

    elif status_code == 404:
        print("Error 404: Resource Not Found.")

    elif status_code == 500:
        print("Error 500: Internal Server Error.")

    else:
        print(f"Unexpected API error: HTTP {status_code}")

    return None


successful_response = {
    "id": 1,
    "name": "Teja",
    "course": "Python AI/ML"
}

result = handle_api_response(200, successful_response)

print("Response:", result)


print("\n=== 2. Handling 400 Bad Request ===")

handle_api_response(
    400,
    {"error": "Invalid request data"}
)


print("\n=== 3. Handling 401 Unauthorized ===")

handle_api_response(
    401,
    {"error": "Authentication required"}
)


print("\n=== 4. Handling 403 Forbidden ===")

handle_api_response(
    403,
    {"error": "Access denied"}
)


print("\n=== 5. Handling 404 Not Found ===")

handle_api_response(
    404,
    {"error": "Resource not found"}
)


print("\n=== 6. Handling 500 Server Error ===")

handle_api_response(
    500,
    {"error": "Internal server error"}
)


print("\n=== 7. Handling Invalid JSON Response ===")


def parse_json_response(response_text):
    try:
        return json.loads(response_text)

    except json.JSONDecodeError:
        print("Error: Invalid JSON response.")
        return None


valid_json = '{"name": "Teja", "score": 85}'

parsed_data = parse_json_response(valid_json)

print("Parsed response:", parsed_data)


invalid_json = '{"name": "Teja", "score": 85'

parsed_invalid_data = parse_json_response(invalid_json)

print("Parsed invalid response:", parsed_invalid_data)


print("\n=== 8. Safe API Processing ===")


def process_api_response(status_code, response_text):
    if status_code != 200:
        handle_api_response(status_code, None)
        return None

    data = parse_json_response(response_text)

    if data is None:
        print("API response could not be processed.")
        return None

    print("API response processed successfully.")
    return data


api_result = process_api_response(
    200,
    '{"name": "Ajay", "course": "Data Science"}'
)

print("Final result:", api_result)


print("\n=== 9. API Error Handling Summary ===")

print("HTTP status codes handled.")
print("Client errors handled.")
print("Server errors handled.")
print("Invalid JSON responses handled.")
print("API processing failures handled safely.")
print("Reusable API error-handling functions created.")