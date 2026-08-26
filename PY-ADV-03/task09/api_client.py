# PY-ADV-03 - Task 9
# Consume a REST API using Python

import json
from urllib.request import urlopen


API_URL = "https://jsonplaceholder.typicode.com/users"


print("=== 1. REST API Request ===")

print("API URL:", API_URL)


try:
    with urlopen(API_URL) as response:
        data = response.read().decode("utf-8")

    print("API request successful.")
    print("Response received.")

except Exception as error:
    print("API request failed:", error)
    data = None


print("\n=== 2. Parsing API Response ===")

if data:
    users = json.loads(data)

    print("Number of users:", len(users))


print("\n=== 3. Processing API Data ===")

if data:
    for user in users:
        print(
            f"ID: {user['id']} | "
            f"Name: {user['name']} | "
            f"Email: {user['email']}"
        )


print("\n=== 4. Accessing Nested API Data ===")

if data:
    first_user = users[0]

    print("Name:", first_user["name"])
    print("City:", first_user["address"]["city"])
    print("Company:", first_user["company"]["name"])


print("\n=== 5. REST API Summary ===")

if data:
    print("REST API consumed successfully.")
    print("JSON response received.")
    print("Response parsed successfully.")
    print("API records processed successfully.")
    print("Nested API data accessed successfully.")
else:
    print("API data could not be processed.")