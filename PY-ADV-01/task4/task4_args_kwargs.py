# PY-ADV-01 - Task 4
# Practice *args and **kwargs


print("=== 1. Using *args ===")


def add_numbers(*args):
    print("Arguments received:", args)
    print("Type of args:", type(args))

    return sum(args)


print("Sum:", add_numbers(10, 20))
print("Sum:", add_numbers(10, 20, 30, 40))


print("\n=== 2. Finding Maximum Using *args ===")


def find_maximum(*args):

    if not args:
        return None

    return max(args)


print("Maximum:", find_maximum(10, 50, 20, 40))
print("Maximum:", find_maximum(100, 25, 75))


print("\n=== 3. Using **kwargs ===")


def show_details(**kwargs):

    print("Details received:", kwargs)
    print("Type of kwargs:", type(kwargs))

    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_details(
    name="Teja",
    age=25,
    course="Python AI/ML"
)


print("\n=== 4. Combining *args and **kwargs ===")


def display_information(*args, **kwargs):

    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


display_information(
    10,
    20,
    30,
    name="Teja",
    role="Python Developer"
)


print("\n=== 5. Practical Example ===")


def calculate_total(*prices, discount=0):

    total = sum(prices)

    discount_amount = total * discount / 100

    final_amount = total - discount_amount

    return final_amount


print("Total:", calculate_total(100, 200, 300))
print("Total after discount:", calculate_total(100, 200, 300, discount=10))