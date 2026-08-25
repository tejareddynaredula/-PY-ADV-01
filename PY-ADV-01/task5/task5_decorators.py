# PY-ADV-01 - Task 5
# Implement Decorators


print("=== 1. Basic Decorator ===")


def simple_decorator(function):

    def wrapper():
        print("Before function execution")
        function()
        print("After function execution")

    return wrapper


@simple_decorator
def greet():
    print("Hello, Teja!")


greet()


print("\n=== 2. Decorator with Function Arguments ===")


def logging_decorator(function):

    def wrapper(*args, **kwargs):
        print("Function called:", function.__name__)
        print("Arguments:", args)
        print("Keyword arguments:", kwargs)

        result = function(*args, **kwargs)

        print("Function result:", result)

        return result

    return wrapper


@logging_decorator
def add(a, b):
    return a + b


result = add(10, 20)
print("Final result:", result)


print("\n=== 3. Timing-Style Decorator ===")


def execution_message(function):

    def wrapper(*args, **kwargs):
        print(f"Starting function: {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Finished function: {function.__name__}")

        return result

    return wrapper


@execution_message
def calculate_square(number):
    return number * number


print("Square:", calculate_square(8))


print("\n=== 4. Decorator for Access Control ===")


def require_positive(function):

    def wrapper(number):
        if number <= 0:
            print("Error: Number must be positive.")
            return None

        return function(number)

    return wrapper


@require_positive
def calculate_double(number):
    return number * 2


print("Double:", calculate_double(10))
print("Double:", calculate_double(-5))


print("\n=== 5. Multiple Decorators ===")


def decorator_one(function):

    def wrapper():
        print("Decorator One - Before")
        function()
        print("Decorator One - After")

    return wrapper


def decorator_two(function):

    def wrapper():
        print("Decorator Two - Before")
        function()
        print("Decorator Two - After")

    return wrapper


@decorator_one
@decorator_two
def message():
    print("Inside the original function")


message()