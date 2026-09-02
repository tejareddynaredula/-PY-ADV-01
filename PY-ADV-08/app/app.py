import logging
from flask import Flask, jsonify, request
from database.connection import get_connection

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def employee_data(row):
    return {
        "id": row[0],
        "name": row[1],
        "age": row[2],
        "department": row[3],
        "salary": float(row[4])
    }


@app.route("/", methods=["GET"])
def home():
    logger.info("GET /")
    return jsonify({"message": "Employee REST API is running"})


@app.route("/employees", methods=["GET"])
def get_employees():
    logger.info("GET /employees")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT e.employee_id, e.name, e.age,
               d.department_name, e.salary
        FROM employees e
        JOIN departments d ON e.department_id = d.department_id
        ORDER BY e.employee_id
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify([employee_data(row) for row in rows])


@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    logger.info("GET /employees/%s", employee_id)

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT e.employee_id, e.name, e.age,
               d.department_name, e.salary
        FROM employees e
        JOIN departments d ON e.department_id = d.department_id
        WHERE e.employee_id = %s
    """, (employee_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row is None:
        logger.warning("Employee %s not found", employee_id)
        return jsonify({"error": "Employee not found"}), 404

    return jsonify(employee_data(row))


@app.route("/employees", methods=["POST"])
def create_employee():
    logger.info("POST /employees")

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    required = ["name", "age", "department", "salary"]
    if not all(field in data for field in required):
        return jsonify({"error": "All employee fields are required"}), 400

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT department_id FROM departments WHERE department_name = %s",
        (data["department"],)
    )
    department = cur.fetchone()

    if department is None:
        cur.close()
        conn.close()
        return jsonify({"error": "Department not found"}), 400

    cur.execute("""
        INSERT INTO employees (name, age, department_id, salary)
        VALUES (%s, %s, %s, %s)
        RETURNING employee_id
    """, (data["name"], data["age"], department[0], data["salary"]))

    employee_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    logger.info("Employee %s created", employee_id)

    return jsonify({
        "id": employee_id,
        "name": data["name"],
        "age": data["age"],
        "department": data["department"],
        "salary": data["salary"]
    }), 201


@app.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    logger.info("PUT /employees/%s", employee_id)

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    required = ["name", "age", "department", "salary"]
    if not all(field in data for field in required):
        return jsonify({"error": "All employee fields are required"}), 400

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT department_id FROM departments WHERE department_name = %s",
        (data["department"],)
    )
    department = cur.fetchone()

    if department is None:
        cur.close()
        conn.close()
        return jsonify({"error": "Department not found"}), 400

    cur.execute("""
        UPDATE employees
        SET name = %s, age = %s, department_id = %s, salary = %s
        WHERE employee_id = %s
    """, (
        data["name"], data["age"], department[0],
        data["salary"], employee_id
    ))

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        logger.warning("Employee %s not found", employee_id)
        return jsonify({"error": "Employee not found"}), 404

    conn.commit()
    cur.close()
    conn.close()

    logger.info("Employee %s updated", employee_id)

    return jsonify({
        "id": employee_id,
        "name": data["name"],
        "age": data["age"],
        "department": data["department"],
        "salary": data["salary"]
    })


@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    logger.info("DELETE /employees/%s", employee_id)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM employees WHERE employee_id = %s",
        (employee_id,)
    )

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        logger.warning("Employee %s not found", employee_id)
        return jsonify({"error": "Employee not found"}), 404

    conn.commit()
    cur.close()
    conn.close()

    logger.info("Employee %s deleted", employee_id)

    return jsonify({"message": "Employee deleted successfully"})


@app.errorhandler(404)
def not_found(error):
    logger.warning("Resource not found")
    return jsonify({"error": "Resource not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)