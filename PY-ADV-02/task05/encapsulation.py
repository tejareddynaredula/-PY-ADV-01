# PY-ADV-02 - Task 5
# Encapsulation


class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.__balance = initial_balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.__balance += amount
        print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        if amount > self.__balance:
            print("Insufficient balance.")
            return

        self.__balance -= amount
        print("Withdrawal successful.")

    def display_account(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.__balance)


print("=== 1. Creating Bank Account ===")

account = BankAccount("Teja", 10000)
account.display_account()


print("\n=== 2. Accessing Encapsulated Data ===")

print("Account Holder:", account.account_holder)
print("Balance:", account.balance)


print("\n=== 3. Depositing Money ===")

account.deposit(5000)
print("Updated Balance:", account.balance)


print("\n=== 4. Withdrawing Money ===")

account.withdraw(3000)
print("Updated Balance:", account.balance)


print("\n=== 5. Preventing Invalid Withdrawal ===")

account.withdraw(20000)
print("Balance:", account.balance)


print("\n=== 6. Preventing Invalid Deposit ===")

account.deposit(-1000)
print("Balance:", account.balance)


print("\n=== 7. Private Attribute Protection ===")

try:
    print(account.__balance)
except AttributeError:
    print("Direct access to private balance is not allowed.")


print("\n=== 8. Final Account Details ===")

account.display_account()