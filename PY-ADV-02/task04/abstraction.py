# PY-ADV-02 - Task 4
# Abstraction

from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_role(self):
        pass

    def display_basic_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

    def display_role(self):
        return "Full-Time Employee"


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def display_role(self):
        return "Part-Time Employee"


print("=== 1. Full-Time Employee ===")

full_time = FullTimeEmployee(
    "Teja",
    "EMP001",
    60000
)

full_time.display_basic_details()
print("Role:", full_time.display_role())
print("Salary:", full_time.calculate_salary())


print("\n=== 2. Part-Time Employee ===")

part_time = PartTimeEmployee(
    "Sumanth",
    "EMP002",
    500,
    80
)

part_time.display_basic_details()
print("Role:", part_time.display_role())
print("Salary:", part_time.calculate_salary())


print("\n=== 3. Abstraction Through Common Interface ===")

employees = [full_time, part_time]

for employee in employees:
    print("\nEmployee:", employee.name)
    print("Role:", employee.display_role())
    print("Salary:", employee.calculate_salary())


print("\n=== 4. Abstract Class Protection ===")

try:
    employee = Employee("Test Employee", "EMP003")
except TypeError:
    print("Cannot create an object of the abstract Employee class.")