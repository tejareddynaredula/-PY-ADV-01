# Student Management System

## Overview

A Python-based Student Management System demonstrating clean project structure, object-oriented programming, validation, exception handling, logging, type hints, documentation, and unit testing.

## Features

- Add students
- View all students
- Find students by ID
- Update student details
- Delete students
- Validate student information
- Handle student-not-found errors
- Log student operations
- Unit testing

## Project Structure

```text
PY-ADV-06/
|-- app/
|   |-- config/
|   |   |-- __init__.py
|   |   `-- settings.py
|   |-- exceptions/
|   |   |-- __init__.py
|   |   `-- student_exceptions.py
|   |-- models/
|   |   |-- __init__.py
|   |   `-- student.py
|   |-- services/
|   |   |-- __init__.py
|   |   `-- student_service.py
|   `-- utils/
|       |-- helpers.py
|       `-- logger.py
|-- tests/
|   `-- test_student.py
|-- main.py
|-- requirements.txt
|-- README.md
`-- .gitignore
## Technologies

- Python
- Object-Oriented Programming
- Python Logging
- unittest
- Type Hints
- PEP 8

## Running the Application

From the `PY-ADV-06` directory:

```text
python main.py