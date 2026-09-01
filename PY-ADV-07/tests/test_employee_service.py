import unittest

from app.services.employee_service import (
    create_employee,
    get_employee,
    get_all_employees,
    update_employee,
    delete_employee,
    search_employee,
)


class TestEmployeeService(unittest.TestCase):

    def test_get_employee(self):
        employee = get_employee(1)

        self.assertIsNotNone(employee)
        self.assertEqual(employee[1], "Teja")

    def test_get_all_employees(self):
        employees = get_all_employees()

        self.assertGreaterEqual(len(employees), 4)

    def test_create_employee(self):
        create_employee("Test Employee", 26, 1, 40000.00)

        employees = search_employee("Test Employee")

        self.assertTrue(len(employees) > 0)

        employee_id = employees[0][0]

        delete_employee(employee_id)

    def test_update_employee(self):
        create_employee("Update Test", 25, 1, 40000.00)

        employees = search_employee("Update Test")
        employee_id = employees[0][0]

        update_employee(
            employee_id,
            "Updated Employee",
            26,
            2,
            45000.00,
        )

        employee = get_employee(employee_id)

        self.assertEqual(employee[1], "Updated Employee")
        self.assertEqual(employee[2], 26)

        delete_employee(employee_id)

    def test_delete_employee(self):
        create_employee("Delete Test", 25, 1, 40000.00)

        employees = search_employee("Delete Test")
        employee_id = employees[0][0]

        delete_employee(employee_id)

        employee = get_employee(employee_id)

        self.assertIsNone(employee)

    def test_search_employee(self):
        employees = search_employee("Teja")

        self.assertTrue(len(employees) > 0)
        self.assertEqual(employees[0][1], "Teja")


if __name__ == "__main__":
    unittest.main()