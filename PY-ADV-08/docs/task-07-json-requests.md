# Task 7 - Accept JSON Requests

## Objective

Accept JSON data from API requests.

## Implementation

The API uses Flask's request.get_json() to read JSON request data.

If JSON data is missing or empty, the API returns a 400 Bad Request response.

## Example JSON

{
    "name": "Priya",
    "age": 28,
    "department": "Finance",
    "salary": 60000
}

## Testing

Valid JSON request: 201 Created

Empty JSON request: 400 Bad Request

## Key Takeaway

Flask can read JSON request data using request.get_json().
