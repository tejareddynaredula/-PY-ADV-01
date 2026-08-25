# PY-ADV-02 - Task 7
# Class Methods and Static Methods


class Employee:
    company_name = "Tech Solutions"
    employee_count = 0

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        Employee.employee_count += 1

    # Instance method
    def display_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)

    # Class method
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

    # Class method
    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

    # Static method
    @staticmethod
    def is_valid_salary(salary):
        return salary > 0


print("=== 1. Creating Employees ===")

employee1 = Employee("Teja", "EMP001", 60000)
employee2 = Employee("Sumanth", "EMP002", 50000)

print("Employees created successfully.")


print("\n=== 2. Instance Method ===")

employee1.display_details()


print("\n=== 3. Class Variable ===")

print("Company Name:", Employee.company_name)


print("\n=== 4. Class Method ===")

Employee.change_company_name("AI Solutions")

print("Updated Company Name:", Employee.company_name)


print("\n=== 5. Employee Count ===")

print("Total Employees:", Employee.get_employee_count())


print("\n=== 6. Static Method ===")

print("Is 50000 a valid salary?", Employee.is_valid_salary(50000))
print("Is -1000 a valid salary?", Employee.is_valid_salary(-1000))


print("\n=== 7. Static Method Through Object ===")

print("Is 75000 a valid salary?", employee1.is_valid_salary(75000))


print("\n=== 8. Final Employee Details ===")

employee1.display_details()
employee2.display_details()
print("Company Name:", Employee.company_name)
print("Total Employees:", Employee.get_employee_count())