# PY-ADV-03 - Task 11
# Implement Timeout Handling

import requests


print("=== 1. Successful Request with Timeout ===")


def make_request(url, timeout_seconds=5):
    try:
        response = requests.get(
            url,
            timeout=timeout_seconds
        )

        print("Request completed successfully.")
        print("Status Code:", response.status_code)

        return response

    except requests.exceptions.Timeout:
        print("Error: API request timed out.")
        return None

    except requests.exceptions.RequestException as error:
        print("Error: API request failed.")
        print("Details:", error)
        return None


response = make_request(
    "https://httpbin.org/get",
    timeout_seconds=5
)

if response is not None:
    print("Response received successfully.")


print("\n=== 2. Simulating a Timeout ===")


timeout_response = make_request(
    "https://httpbin.org/delay/10",
    timeout_seconds=2
)

if timeout_response is None:
    print("Timeout was handled safely.")


print("\n=== 3. Different Timeout Values ===")


def test_timeout(url, timeout_seconds):
    print(
        f"Testing request with timeout "
        f"of {timeout_seconds} seconds..."
    )

    try:
        response = requests.get(
            url,
            timeout=timeout_seconds
        )

        print("Request completed.")
        print("Status Code:", response.status_code)

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.RequestException as error:
        print("Request failed:", error)


test_timeout(
    "https://httpbin.org/get",
    5
)


print("\n=== 4. Timeout Handling Summary ===")

print("Timeout value configured.")
print("API request executed with timeout.")
print("Timeout exception handled.")
print("Request errors handled.")
print("Application continues safely after timeout.")