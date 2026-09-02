# Employee REST API Documentation

## Overview

The Employee REST API is a Flask-based REST API connected to a PostgreSQL database.

It provides CRUD operations for managing employee records.

## Technologies

- Python
- Flask
- PostgreSQL
- Psycopg
- JSON
- Postman

## Base URL

```text
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/employees` | Get all employees |
| GET | `/employees/<id>` | Get one employee |
| POST | `/employees` | Create an employee |
| PUT | `/employees/<id>` | Update an employee |
| DELETE | `/employees/<id>` | Delete an employee |

## Request Format

POST and PUT requests use JSON.

Example:

```json
{
  "name": "John",
  "age": 30,
  "department": "IT",
  "salary": 50000
}
```

Required fields:

- name
- age
- department
- salary

## Response Format

Successful responses are returned as JSON.

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

## HTTP Status Codes

| Status Code | Meaning |
|---|---|
| 200 | Request successful |
| 201 | Employee created |
| 400 | Invalid request |
| 404 | Resource not found |

## Database

The API uses the PostgreSQL database:

```text
employee_management
```

Employee data is stored in the `employees` table and department information is stored in the `departments` table.

## Configuration

The PostgreSQL password is read from the environment variable:

```text
POSTGRES_PASSWORD
```

## Running the API

Navigate to the application directory:

```powershell
cd .\PY-ADV-08\app
```

Then start the Flask API:

```powershell
python -m flask --app .\app.py run --host 0.0.0.0 --port 5000
```

The API will be available at:

```text
http://127.0.0.1:5000
```

## Postman Testing

The API was tested using Postman.

The Postman collection is available at:

```text
PY-ADV-08/postman/Employee REST API.postman_collection.json
```

The main CRUD operations were tested successfully.

## Logging

The application uses Python's built-in logging module to record API requests and employee operations.

## Conclusion

The Employee REST API provides a simple interface for performing CRUD operations on employee data using Flask and PostgreSQL.