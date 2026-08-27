import time


def inefficient_processing(numbers):
    result = []

    for number in numbers:
        if number % 2 == 0:
            result.append(number * 2)

    return result


def optimized_processing(numbers):
    return [number * 2 for number in numbers if number % 2 == 0]


numbers = list(range(1, 1000000))

start = time.perf_counter()
inefficient_result = inefficient_processing(numbers)
inefficient_time = time.perf_counter() - start

start = time.perf_counter()
optimized_result = optimized_processing(numbers)
optimized_time = time.perf_counter() - start


print("=== PY-ADV-04 Task 5: Loop Optimization ===")

print("\nInefficient approach:")
print(f"Execution time: {inefficient_time:.6f} seconds")

print("\nOptimized approach:")
print(f"Execution time: {optimized_time:.6f} seconds")

print("\nResults are equal:", inefficient_result == optimized_result)

if optimized_time < inefficient_time:
    print("Optimized approach was faster.")
else:
    print("Inefficient approach was faster.")

print("\nOptimization applied:")
print("- Reduced explicit loop code.")
print("- Used list comprehension for data processing.")