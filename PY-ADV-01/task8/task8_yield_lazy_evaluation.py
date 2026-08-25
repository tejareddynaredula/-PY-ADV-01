# PY-ADV-01 - Task 8
# yield and Lazy Evaluation


print("=== 1. yield Pauses Function Execution ===")


def simple_generator():

    print("Step 1: Function started")

    yield 10

    print("Step 2: Resuming function")

    yield 20

    print("Step 3: Resuming function again")

    yield 30

    print("Step 4: Function completed")


generator = simple_generator()

print("Generator created.")

print("First value:", next(generator))
print("Second value:", next(generator))
print("Third value:", next(generator))


print("\n=== 2. Lazy Evaluation ===")


def lazy_numbers(limit):

    number = 1

    while number <= limit:

        print("Generating:", number)

        yield number

        number += 1


numbers = lazy_numbers(5)

print("Generator created.")

print("Requesting first value...")
print("Value:", next(numbers))

print("Requesting second value...")
print("Value:", next(numbers))

print("Requesting third value...")
print("Value:", next(numbers))


print("\n=== 3. Generator vs List ===")


def generate_squares(limit):

    for number in range(1, limit + 1):

        yield number * number


square_generator = generate_squares(5)

print("Generator type:", type(square_generator))

for square in square_generator:

    print("Generated square:", square)


square_list = [number * number for number in range(1, 6)]

print("List type:", type(square_list))
print("List:", square_list)


print("\n=== 4. Large Data Example ===")


def large_data_generator(limit):

    for number in range(1, limit + 1):

        yield number


large_generator = large_data_generator(1000000)

print("Large generator created.")

print("First value:", next(large_generator))
print("Second value:", next(large_generator))
print("Third value:", next(large_generator))

print("Only requested values were generated.")


print("\n=== 5. Lazy Data Processing ===")


def process_data(data):

    for value in data:

        print("Processing:", value)

        yield value * 2


data = process_data(range(1, 6))

print("Processing started.")

print("Result:", next(data))
print("Result:", next(data))
print("Result:", next(data))