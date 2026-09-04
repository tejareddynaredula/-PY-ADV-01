from flask import Flask, request, jsonify
import sys
import logging
import os

sys.path.insert(0, "PY-ADV-10")

from database.db import create_table
from services.employee_service import (
    create_employee, update_employee, delete_employee,
    search_employee, list_employees
)

app = Flask(__name__)
create_table()

# Logging setup
log_dir = "PY-ADV-10/logs"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=f"{log_dir}/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def validate(data):
    required = ["name", "age", "department", "salary"]
    return all(field in data for field in required)


@app.route("/employees", methods=["GET"])
def get_employees():
    try:
        logger.info("Fetching all employees")
        return jsonify(list_employees())
    except Exception as e:
        logger.error("Error fetching employees: %s", e)
        return jsonify({"error": str(e)}), 500


@app.route("/employees", methods=["POST"])
def add_employee():
    try:
        data = request.json

        if not data or not validate(data):
            logger.warning("Invalid employee data received")
            return jsonify({"error": "Missing required fields"}), 400

        create_employee(
            data["name"], data["age"],
            data["department"], data["salary"]
        )

        logger.info("Employee created: %s", data["name"])
        return jsonify({"message": "Employee created"}), 201

    except Exception as e:
        logger.error("Error creating employee: %s", e)
        return jsonify({"error": str(e)}), 500


@app.route("/employees/<int:employee_id>", methods=["PUT"])
def edit_employee(employee_id):
    try:
        data = request.json

        if not data or not validate(data):
            logger.warning("Invalid update data for employee %s", employee_id)
            return jsonify({"error": "Missing required fields"}), 400

        update_employee(
            employee_id, data["name"], data["age"],
            data["department"], data["salary"]
        )

        logger.info("Employee updated: %s", employee_id)
        return jsonify({"message": "Employee updated"})

    except Exception as e:
        logger.error("Error updating employee: %s", e)
        return jsonify({"error": str(e)}), 500


@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def remove_employee(employee_id):
    try:
        delete_employee(employee_id)

        logger.info("Employee deleted: %s", employee_id)
        return jsonify({"message": "Employee deleted"})

    except Exception as e:
        logger.error("Error deleting employee: %s", e)
        return jsonify({"error": str(e)}), 500


@app.route("/employees/search/<name>", methods=["GET"])
def find_employee(name):
    try:
        logger.info("Searching employee: %s", name)
        return jsonify(search_employee(name))

    except Exception as e:
        logger.error("Error searching employee: %s", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)