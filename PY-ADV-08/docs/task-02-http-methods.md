# Task 2 - Understand HTTP Methods

## Objective

Understand the HTTP methods used by REST APIs to perform different operations on resources.

## HTTP Methods

| Method | Purpose | Employee API Example |
|---|---|---|
| GET | Retrieve data | Get all employees |
| POST | Create new data | Add a new employee |
| PUT | Replace or update existing data | Update an employee |
| PATCH | Partially update data | Change only an employee's salary |
| DELETE | Delete data | Delete an employee |

## GET

GET is used to retrieve data from the server.

Example:

GET /employees

This requests the list of all employees.

## POST

POST is used to create a new resource.

Example:

POST /employees

This creates a new employee.

## PUT

PUT is used to completely update or replace an existing resource.

Example:

PUT /employees/1

This updates employee with ID 1.

## PATCH

PATCH is used to partially update an existing resource.

Example:

PATCH /employees/1

This can be used to update only selected employee information.

## DELETE

DELETE is used to remove a resource.

Example:

DELETE /employees/1

This deletes employee with ID 1.

## Key Takeaways

- GET is used to read data.
- POST is used to create data.
- PUT is used to replace or update data.
- PATCH is used for partial updates.
- DELETE is used to remove data.