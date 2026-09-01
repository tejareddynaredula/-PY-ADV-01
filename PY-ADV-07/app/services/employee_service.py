from app.database.db_utils import execute_query, fetch_all, fetch_one


def create_employee(name: str, age: int, department_id: int, salary: float) -> None:
    """Create a new employee."""
    query = """
        INSERT INTO employees (name, age, department_id, salary)
        VALUES (%s, %s, %s, %s)
    """
    execute_query(query, (name, age, department_id, salary))


def get_employee(employee_id: int):
    """Get one employee by ID."""
    query = """
        SELECT employee_id, name, age, department_id, salary
        FROM employees
        WHERE employee_id = %s
    """
    return fetch_one(query, (employee_id,))


def get_all_employees():
    """Get all employees."""
    query = """
        SELECT employee_id, name, age, department_id, salary
        FROM employees
        ORDER BY employee_id
    """
    return fetch_all(query)


def update_employee(
    employee_id: int,
    name: str,
    age: int,
    department_id: int,
    salary: float,
) -> None:
    """Update an employee."""
    query = """
        UPDATE employees
        SET name = %s,
            age = %s,
            department_id = %s,
            salary = %s
        WHERE employee_id = %s
    """
    execute_query(
        query,
        (name, age, department_id, salary, employee_id),
    )


def delete_employee(employee_id: int) -> None:
    """Delete an employee."""
    query = """
        DELETE FROM employees
        WHERE employee_id = %s
    """
    execute_query(query, (employee_id,))


def search_employee(search_term: str):
    """Search employees by name."""
    query = """
        SELECT employee_id, name, age, department_id, salary
        FROM employees
        WHERE name ILIKE %s
        ORDER BY employee_id
    """
    return fetch_all(query, (f"%{search_term}%",))