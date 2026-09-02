# Task 4 - Understand HTTP Status Codes

## Objective

Understand the HTTP status codes returned by REST APIs to indicate the result of a request.

## Common HTTP Status Codes

| Status Code | Meaning | Employee API Example |
|---|---|---|
| 200 | OK - Request successful | Successfully retrieve employees |
| 201 | Created - Resource created successfully | Successfully create an employee |
| 400 | Bad Request - Invalid request | Missing or invalid employee data |
| 404 | Not Found - Resource does not exist | Employee ID does not exist |
| 500 | Internal Server Error - Server-side error | Unexpected application error |

## 200 - OK

The request was successful.

Example:

GET /employees

The API successfully returns the employee list.

## 201 - Created

A new resource was successfully created.

Example:

POST /employees

The API creates a new employee and returns status 201.

## 400 - Bad Request

The request contains invalid or incorrect data.

Example:

A request is sent without the required employee name.

The API can return status 400.

## 404 - Not Found

The requested resource does not exist.

Example:

GET /employees/999

If employee 999 does not exist, the API can return status 404.

## 500 - Internal Server Error

An unexpected error occurs on the server.

The API can return status 500 when it cannot process the request because of an internal application or server error.

## Key Takeaways

- 200 means the request was successful.
- 201 means a resource was created.
- 400 means the request is invalid.
- 404 means the requested resource was not found.
- 500 means an unexpected server-side error occurred.