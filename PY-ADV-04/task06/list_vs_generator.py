import sys


def create_list():
    return [number * 2 for number in range(100000)]


def create_generator():
    return (number * 2 for number in range(100000))


numbers_list = create_list()
numbers_generator = create_generator()

print("=== PY-ADV-04 Task 6: List vs Generator ===")

print("\n1. List")
print("Type:", type(numbers_list))
print("First 5 values:", numbers_list[:5])
print("Memory size:", sys.getsizeof(numbers_list), "bytes")

print("\n2. Generator")
print("Type:", type(numbers_generator))
print("First 5 values:", [next(numbers_generator) for _ in range(5)])
print("Memory size:", sys.getsizeof(numbers_generator), "bytes")

print("\n3. Comparison")
print("List stores all generated values in memory.")
print("Generator produces values lazily when they are requested.")
print("Generators generally use less memory for large sequences.")

print("\n4. Conclusion")
print("List is useful when values need to be stored and accessed repeatedly.")
print("Generator is useful when values can be processed one at a time.")