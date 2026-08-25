# PY-ADV-02 - Task 10
# Proper Exception-Handling Flows


class InsufficientBalanceError(Exception):
    """Raised when the account has insufficient balance."""
    pass


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > self.balance:
            raise InsufficientBalanceError(
                "Insufficient balance for this withdrawal."
            )

        self.balance -= amount
        return self.balance


def process_withdrawal(account, amount):
    print("Requested withdrawal:", amount)

    try:
        new_balance = account.withdraw(amount)

    except ValueError as error:
        print("Validation Error:", error)

    except InsufficientBalanceError as error:
        print("Account Error:", error)

    except Exception as error:
        print("Unexpected Error:", error)

    else:
        print("Withdrawal successful.")
        print("Remaining Balance:", new_balance)

    finally:
        print("Withdrawal process completed.")


print("=== 1. Creating Bank Account ===")

account = BankAccount("Teja", 10000)

print("Account Holder:", account.account_holder)
print("Initial Balance:", account.balance)


print("\n=== 2. Successful Withdrawal ===")

process_withdrawal(account, 3000)


print("\n=== 3. Invalid Withdrawal ===")

process_withdrawal(account, -500)


print("\n=== 4. Insufficient Balance ===")

process_withdrawal(account, 20000)


print("\n=== 5. Another Successful Withdrawal ===")

process_withdrawal(account, 2000)


print("\n=== 6. Final Account Details ===")

print("Account Holder:", account.account_holder)
print("Final Balance:", account.balance)


print("\n=== 7. Exception Handling Flow ===")

print("try     -> Executes the risky operation.")
print("except  -> Handles specific exceptions.")
print("else    -> Runs when no exception occurs.")
print("finally -> Runs whether an exception occurs or not.")