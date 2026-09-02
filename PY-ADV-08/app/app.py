from flask import Flask, jsonify, request

app = Flask(__name__)


employees = [
    {
        "id": 1,
        "name": "Teja",
        "age": 22,
        "department": "IT",
        "salary": 55000
    },
    {
        "id": 2,
        "name": "Rahul",
        "age": 25,
        "department": "HR",
        "salary": 45000
    }
]


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Employee REST API is running"
    })


@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)


@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    employee = next(
        (employee for employee in employees if employee["id"] == employee_id),
        None
    )

    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify(employee)


@app.route("/employees", methods=["POST"])
def create_employee():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    required = ["name", "age", "department", "salary"]

    if not all(field in data for field in required):
        return jsonify({"error": "All employee fields are required"}), 400

    new_employee = {
        "id": len(employees) + 1,
        "name": data["name"],
        "age": data["age"],
        "department": data["department"],
        "salary": data["salary"]
    }

    employees.append(new_employee)

    return jsonify(new_employee), 201


@app.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    employee = next(
        (employee for employee in employees if employee["id"] == employee_id),
        None
    )

    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    required = ["name", "age", "department", "salary"]

    if not all(field in data for field in required):
        return jsonify({"error": "All employee fields are required"}), 400

    employee["name"] = data["name"]
    employee["age"] = data["age"]
    employee["department"] = data["department"]
    employee["salary"] = data["salary"]

    return jsonify(employee)


@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    employee = next(
        (employee for employee in employees if employee["id"] == employee_id),
        None
    )

    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    employees.remove(employee)

    return jsonify({
        "message": "Employee deleted successfully"
    })


if __name__ == "__main__":
    app.run(debug=True)