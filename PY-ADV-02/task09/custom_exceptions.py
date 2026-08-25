# PY-ADV-02 - Task 9
# Custom Exceptions


class InsufficientBalanceError(Exception):
    """Raised when the account has insufficient balance."""
    pass


class InvalidDepositError(Exception):
    """Raised when the deposit amount is invalid."""
    pass


class InvalidWithdrawalError(Exception):
    """Raised when the withdrawal amount is invalid."""
    pass


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidDepositError(
                "Deposit amount must be greater than zero."
            )

        self.balance += amount
        print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidWithdrawalError(
                "Withdrawal amount must be greater than zero."
            )

        if amount > self.balance:
            raise InsufficientBalanceError(
                "Insufficient balance for this withdrawal."
            )

        self.balance -= amount
        print("Withdrawal successful.")

    def display_balance(self):
        print("Current Balance:", self.balance)


print("=== 1. Creating Bank Account ===")

account = BankAccount("Teja", 10000)

print("Account Holder:", account.account_holder)
account.display_balance()


print("\n=== 2. Successful Deposit ===")

try:
    account.deposit(5000)
    account.display_balance()
except InvalidDepositError as error:
    print("Error:", error)


print("\n=== 3. Invalid Deposit ===")

try:
    account.deposit(-1000)
except InvalidDepositError as error:
    print("Error:", error)


print("\n=== 4. Successful Withdrawal ===")

try:
    account.withdraw(3000)
    account.display_balance()
except (InvalidWithdrawalError, InsufficientBalanceError) as error:
    print("Error:", error)


print("\n=== 5. Insufficient Balance ===")

try:
    account.withdraw(20000)
except InsufficientBalanceError as error:
    print("Error:", error)


print("\n=== 6. Invalid Withdrawal ===")

try:
    account.withdraw(0)
except InvalidWithdrawalError as error:
    print("Error:", error)


print("\n=== 7. Custom Exceptions Summary ===")

print("InsufficientBalanceError -> Handles insufficient balance.")
print("InvalidDepositError -> Handles invalid deposits.")
print("InvalidWithdrawalError -> Handles invalid withdrawals.")


print("\n=== 8. Final Account Details ===")

print("Account Holder:", account.account_holder)
account.display_balance()