# Task 6 - Create API Routes

## Objective

Create and test REST API routes for managing employee resources.

## Employee API Routes

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /employees | Retrieve all employees |
| POST | /employees | Create a new employee |
| GET | /employees/<id> | Retrieve one employee |
| PUT | /employees/<id> | Update an employee |
| DELETE | /employees/<id> | Delete an employee |

## Implementation

The Flask application implements the required employee routes using Flask route decorators.

The API returns JSON responses and appropriate HTTP status codes.

## Testing Results

| Route | Result |
|---|---|
| GET /employees | 200 OK |
| GET /employees/1 | 200 OK |
| POST /employees | 201 Created |
| PUT /employees/3 | 200 OK |
| DELETE /employees/3 | 200 OK |

A temporary employee was created for POST and PUT testing and was deleted after testing.

## Key Takeaways

- Flask routes map URLs to Python functions.
- HTTP methods determine the operation performed.
- Route parameters allow individual employees to be accessed by ID.
- API responses are returned as JSON.
- HTTP status codes indicate the result of each request.