1.
Custom
Exception
for Invalid Age:
    class InvalidVoterException(Exception):
        pass


def check_age(age):
    if age < 18:
        raise InvalidVoterException("You are not eligible to vote.")
    else:
        print("You are eligible to vote.")


age = int(input("Enter your age: "))
try:
    check_age(age)
except InvalidVoterException as e:
    print(e)
2.
Custom
Exception
for Salary Out of Range:
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
    employee = Employee("Alice", 15000)
except SalaryNotInRangeException as e:
    print(e)
3.
Handling
Division
by
Zero and Index
Errors:
arr = [10, 5, 15, 20]

divisor = int(input("Enter a divisor: "))

try:
    for i in range(len(arr)):
        result = arr[i] / divisor
        print(f"{arr[i]} / {divisor} = {result}")
except ZeroDivisionError:
    print("Error: Division by zero")
except IndexError:
    print("Error: Index out of range")
except ValueError:
    print("Error: Invalid input")
4.
Custom
Exception
for Insufficient Balance:
    class InsufficientFundsException(Exception):
        pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException("Insufficient funds")
        self.balance -= amount
        print(f"Withdrew {amount}. Current balance: {self.balance}")


account = BankAccount(1000)
try:
    account.withdraw(1500)
except InsufficientFundsException as e:
    print(e)