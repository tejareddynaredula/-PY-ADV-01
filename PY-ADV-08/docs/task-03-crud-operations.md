# Task 3 - CRUD Operations with HTTP Methods

## Objective

Understand how HTTP methods are used to perform CRUD operations in a REST API.

## What is CRUD?

CRUD stands for:

- Create
- Read
- Update
- Delete

These operations are mapped to HTTP methods in REST APIs.

| CRUD Operation | HTTP Method | Endpoint | Purpose |
|---|---|---|---|
| Create | POST | /employees | Create a new employee |
| Read | GET | /employees | Get all employees |
| Read | GET | /employees/1 | Get employee with ID 1 |
| Update | PUT | /employees/1 | Update employee with ID 1 |
| Partial Update | PATCH | /employees/1 | Update selected employee fields |
| Delete | DELETE | /employees/1 | Delete employee with ID 1 |

## Create - POST

POST is used to create a new employee.

Example:

POST /employees

Example JSON request:

```json
{
    "name": "Rahul",
    "age": 25,
    "department": "IT",
    "salary": 45000
}
```

## Read - GET

GET is used to retrieve employee information.

Get all employees:

GET /employees

Get one employee:

GET /employees/1

## Update - PUT

PUT is used to completely update or replace an employee's information.

Example:

PUT /employees/1

## Partial Update - PATCH

PATCH is used when only some information needs to be changed.

Example:

PATCH /employees/1

For example, only the salary can be updated.

## Delete - DELETE

DELETE is used to remove an employee.

Example:

DELETE /employees/1

## Key Takeaways

- POST is used to create data.
- GET is used to read data.
- PUT is used to replace or update data.
- PATCH is used for partial updates.
- DELETE is used to remove data.
- These operations form the basic CRUD functionality of a REST API.