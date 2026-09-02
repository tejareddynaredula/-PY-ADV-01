# Task 9 - Request Validation

## Objective

Validate required employee fields in API requests.

## Required Fields

- name
- age
- department
- salary

## Implementation

The API checks whether all required fields are present before creating or updating an employee.

## Testing

A request missing the salary field returned:

400 Bad Request

Error: All employee fields are required.

## Key Takeaway

Request validation prevents incomplete employee data from being accepted.
