CREATE DATABASE employee_management;

-- Connect to employee_management before running the following statements.

CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INTEGER NOT NULL,
    department_id INTEGER NOT NULL,
    salary NUMERIC(10, 2) NOT NULL,
    CONSTRAINT employees_department_id_fkey
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);