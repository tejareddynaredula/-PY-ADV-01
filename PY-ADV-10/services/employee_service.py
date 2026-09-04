from database.db import get_connection


def create_employee(name, age, department, salary):
    conn = get_connection()
    conn.execute(
        "INSERT INTO employees (name, age, department, salary) VALUES (?, ?, ?, ?)",
        (name, age, department, salary)
    )
    conn.commit()
    conn.close()


def update_employee(employee_id, name, age, department, salary):
    conn = get_connection()
    conn.execute(
        "UPDATE employees SET name=?, age=?, department=?, salary=? WHERE id=?",
        (name, age, department, salary, employee_id)
    )
    conn.commit()
    conn.close()


def delete_employee(employee_id):
    conn = get_connection()
    conn.execute("DELETE FROM employees WHERE id=?", (employee_id,))
    conn.commit()
    conn.close()


def search_employee(name):
    conn = get_connection()
    result = conn.execute(
        "SELECT * FROM employees WHERE name LIKE ?",
        (f"%{name}%",)
    ).fetchall()
    conn.close()
    return result


def list_employees():
    conn = get_connection()
    result = conn.execute("SELECT * FROM employees").fetchall()
    conn.close()
    return result