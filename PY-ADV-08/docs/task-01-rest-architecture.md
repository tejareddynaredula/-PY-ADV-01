# Task 1 - Understand REST Architecture

## Objective

Understand the fundamentals of REST architecture and how REST APIs enable communication between clients and servers.

## What is REST?

REST stands for **Representational State Transfer**.

REST is an architectural style used for designing web APIs that allow different applications to communicate with each other over HTTP.

## Client-Server Communication

A REST API follows a client-server model:

Client -> HTTP Request -> REST API -> HTTP Response -> Client

For this project:

Client -> Flask API -> Employee Service -> Database

The client can be a web application, mobile application, Postman, or another service.

## REST Resources

REST APIs represent data as resources.

For the Employee API, the main resource is:

`/employees`

Individual employees can be accessed using an ID:

`/employees/1`

## HTTP Methods

REST APIs use HTTP methods to perform operations on resources.

| Method | Purpose |
|---|---|
| GET | Retrieve data |
| POST | Create new data |
| PUT | Update/replace existing data |
| PATCH | Partially update data |
| DELETE | Delete data |

## JSON Data

REST APIs commonly use JSON to exchange data.

Example:

```json
{
    "id": 1,
    "name": "Teja",
    "age": 22,
    "department": "IT",
    "salary": 55000
}
```

## Example Request

```http
GET /employees
```

This request asks the API to return the list of employees.

## Example Response

```json
[
    {
        "id": 1,
        "name": "Teja",
        "age": 22,
        "department": "IT"
    }
]
```

## Key Takeaways

- REST is an architectural style for designing APIs.
- REST APIs use HTTP for communication.
- Data is organized as resources.
- HTTP methods define the operation performed on a resource.
- JSON is commonly used for request and response data.
- Flask will be used to build the Employee REST API in this assignment.