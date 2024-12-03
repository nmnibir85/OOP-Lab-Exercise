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
    account.withdraw(1500)  # Attempt to withdraw more than the balance
except InsufficientFundsException as e:
    print(e)
