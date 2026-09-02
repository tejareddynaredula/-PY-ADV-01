# Task 12 - CRUD Endpoints

## Objective

Implement CRUD operations using PostgreSQL.

## Implementation

The Flask API now uses PostgreSQL for employee data.

- GET retrieves employees from the database.
- POST creates an employee.
- PUT updates an employee.
- DELETE removes an employee.
- Department names are mapped to department IDs.

## Testing

| Operation | Result |
|---|---|
| GET /employees | 200 OK |
| GET /employees/1 | 200 OK |
| POST /employees | 201 Created |
| PUT /employees/1 | 200 OK |
| DELETE /employees/4 | 200 OK |
| GET /employees/999 | 404 Not Found |

All CRUD operations were tested successfully.

## Key Takeaway

The Flask REST API can perform CRUD operations directly on PostgreSQL data.
