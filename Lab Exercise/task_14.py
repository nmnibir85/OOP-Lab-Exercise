class SalaryNotInRangeException(Exception):
    pass

class Employee:
    def __init__(self, name, salary):
        if 19000 <= salary <= 50000:
            self.name = name
            self.salary = salary
        else:
            raise SalaryNotInRangeException("Salary should be between 19000 and 50000.")

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

try:
    employee = Employee("Alice", 15000)  # Example with out-of-range salary
except SalaryNotInRangeException as e:
    print(e)
