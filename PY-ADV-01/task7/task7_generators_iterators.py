# PY-ADV-01 - Task 7
# Generators and Iterators


print("=== 1. Basic Generator ===")


def simple_generator():

    yield 1
    yield 2
    yield 3


generator = simple_generator()

print("Type:", type(generator))

print("Value:", next(generator))
print("Value:", next(generator))
print("Value:", next(generator))


print("\n=== 2. Generator with Loop ===")


def number_generator(limit):

    number = 1

    while number <= limit:

        yield number

        number += 1


for number in number_generator(5):
    print("Number:", number)


print("\n=== 3. Generator for Even Numbers ===")


def even_numbers(limit):

    for number in range(1, limit + 1):

        if number % 2 == 0:
            yield number


for number in even_numbers(10):
    print("Even:", number)


print("\n=== 4. Generator Expression ===")


squares = (number * number for number in range(1, 6))

print("Type:", type(squares))

for square in squares:
    print("Square:", square)


print("\n=== 5. Custom Iterator ===")


class CountIterator:

    def __init__(self, limit):

        self.current = 1
        self.limit = limit

    def __iter__(self):

        return self

    def __next__(self):

        if self.current <= self.limit:

            value = self.current

            self.current += 1

            return value

        raise StopIteration


counter = CountIterator(5)

print("Iterator values:")

for value in counter:
    print(value)


print("\n=== 6. Generator for Large Data ===")


def data_generator():

    for number in range(1, 6):

        print("Generating:", number)

        yield number


generator = data_generator()

print("Generator created.")

print("First value:", next(generator))
print("Second value:", next(generator))
print("Third value:", next(generator))