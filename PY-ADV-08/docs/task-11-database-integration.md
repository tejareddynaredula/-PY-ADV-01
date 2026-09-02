# Task 11 - Database Integration

## Objective

Connect the Flask API to the PostgreSQL database.

## Implementation

The API uses Psycopg to connect to the employee_management PostgreSQL database.

The database password is read from the POSTGRES_PASSWORD environment variable.

## Testing

Database connection: Successful

Employee table query: Successful

Existing employee records were retrieved successfully.

## Key Takeaway

Flask can connect to PostgreSQL using Psycopg and retrieve database records.
