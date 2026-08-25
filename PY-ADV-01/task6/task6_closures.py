# PY-ADV-01 - Task 6
# Implement Closures


print("=== 1. Basic Closure ===")


def create_greeting(message):

    def greet(name):
        return f"{message}, {name}!"

    return greet


morning_greeting = create_greeting("Good Morning")
evening_greeting = create_greeting("Good Evening")

print(morning_greeting("Teja"))
print(evening_greeting("Teja"))


print("\n=== 2. Closure with Counter ===")


def create_counter():

    count = 0

    def counter():

        nonlocal count

        count += 1

        return count

    return counter


counter = create_counter()

print("Count:", counter())
print("Count:", counter())
print("Count:", counter())


print("\n=== 3. Closure for Multiplier ===")


def create_multiplier(number):

    def multiply(value):
        return value * number

    return multiply


double = create_multiplier(2)
triple = create_multiplier(3)

print("Double:", double(10))
print("Triple:", triple(10))


print("\n=== 4. Independent Closures ===")


counter_one = create_counter()
counter_two = create_counter()

print("Counter One:", counter_one())
print("Counter One:", counter_one())

print("Counter Two:", counter_two())
print("Counter Two:", counter_two())
print("Counter One:", counter_one())


print("\n=== 5. Closure with Configuration ===")


def create_discount_calculator(discount_percentage):

    def calculate(price):

        discount_amount = price * discount_percentage / 100

        return price - discount_amount

    return calculate


discount_10 = create_discount_calculator(10)
discount_20 = create_discount_calculator(20)

print("Price after 10% discount:", discount_10(1000))
print("Price after 20% discount:", discount_20(1000))