# PY-ADV-01 - Task 9
# Custom Iterators


print("=== 1. Basic Custom Iterator ===")


class CountIterator:

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.end:

            value = self.current
            self.current += 1

            return value

        raise StopIteration


counter = CountIterator(1, 5)

for number in counter:
    print("Number:", number)


print("\n=== 2. Iterator Using next() ===")


counter = CountIterator(10, 12)

print("First:", next(counter))
print("Second:", next(counter))
print("Third:", next(counter))


print("\n=== 3. Reverse Iterator ===")


class ReverseIterator:

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):

        if self.current >= 1:

            value = self.current
            self.current -= 1

            return value

        raise StopIteration


reverse = ReverseIterator(5)

for number in reverse:
    print("Reverse:", number)


print("\n=== 4. Even Number Iterator ===")


class EvenIterator:

    def __init__(self, limit):
        self.current = 2
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.limit:

            value = self.current
            self.current += 2

            return value

        raise StopIteration


even_numbers = EvenIterator(10)

for number in even_numbers:
    print("Even:", number)


print("\n=== 5. Handling StopIteration ===")


counter = CountIterator(1, 2)

print("Value:", next(counter))
print("Value:", next(counter))

try:
    print("Value:", next(counter))
except StopIteration:
    print("Iterator has no more values.")


print("\n=== 6. Independent Iterators ===")


iterator_one = CountIterator(1, 3)
iterator_two = CountIterator(10, 12)

print("Iterator One:", next(iterator_one))
print("Iterator One:", next(iterator_one))

print("Iterator Two:", next(iterator_two))
print("Iterator Two:", next(iterator_two))

print("Iterator One:", next(iterator_one))
print("Iterator Two:", next(iterator_two))
print("\n=== 7. Edge Cases ===")

# Start and end are the same
single_value = CountIterator(5, 5)

print("Single value:", next(single_value))

try:
    next(single_value)
except StopIteration:
    print("Single-value iterator completed.")


# Empty range
empty_iterator = CountIterator(5, 1)

try:
    next(empty_iterator)
except StopIteration:
    print("Empty iterator handled correctly.")


# Even iterator with an odd limit
odd_limit_even_iterator = EvenIterator(9)

for number in odd_limit_even_iterator:
    print("Even with odd limit:", number)