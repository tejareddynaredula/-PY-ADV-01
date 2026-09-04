import sys

sys.path.insert(0, "PY-ADV-10")

from services.employee_service import (
    create_employee,
    update_employee,
    delete_employee,
    search_employee,
    list_employees
)


def test_create_employee():
    create_employee("Test User", 25, "IT", 50000)
    employees = search_employee("Test User")
    assert len(employees) > 0


def test_update_employee():
    employees = search_employee("Test User")
    employee_id = employees[0][0]

    update_employee(employee_id, "Updated User", 26, "HR", 55000)

    result = search_employee("Updated User")
    assert len(result) > 0


def test_delete_employee():
    employees = search_employee("Updated User")
    employee_id = employees[0][0]

    delete_employee(employee_id)

    result = search_employee("Updated User")
    assert len(result) == 0


def test_list_employees():
    employees = list_employees()
    assert isinstance(employees, list)