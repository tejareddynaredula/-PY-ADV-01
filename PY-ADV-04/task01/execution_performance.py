# PY-ADV-04 - Task 1
# Understanding Python Execution Performance

import time


print("=== 1. Python Execution Performance ===")


def run_loop():
    total = 0

    for number in range(1, 1_000_001):
        total += number

    return total


start_time = time.perf_counter()

result = run_loop()

end_time = time.perf_counter()

execution_time = end_time - start_time


print("Calculation result:", result)
print("Execution time:", execution_time, "seconds")


print("\n=== 2. Repeated Execution ===")


for i in range(3):

    start_time = time.perf_counter()

    run_loop()

    end_time = time.perf_counter()

    print(
        f"Run {i + 1}: "
        f"{end_time - start_time:.6f} seconds"
    )


print("\n=== 3. Simple Performance Comparison ===")


def calculate_with_loop(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


numbers = list(range(1, 1_000_001))


start_time = time.perf_counter()

loop_result = calculate_with_loop(numbers)

loop_time = time.perf_counter() - start_time


start_time = time.perf_counter()

sum_result = sum(numbers)

sum_time = time.perf_counter() - start_time


print("Loop result:", loop_result)
print("Built-in sum result:", sum_result)

print(f"Loop execution time: {loop_time:.6f} seconds")
print(f"sum() execution time: {sum_time:.6f} seconds")


print("\n=== 4. Performance Observation ===")

if sum_time < loop_time:
    print("Built-in sum() executed faster than the Python loop.")
else:
    print("The Python loop executed faster in this run.")


print("\n=== 5. Performance Summary ===")

print("Execution time was measured using time.perf_counter().")
print("The same operation was executed multiple times.")
print("A Python loop was compared with the built-in sum().")
print("Execution time can vary between runs.")
print("Built-in operations can be faster because they are implemented efficiently.")
print("Performance should be measured before optimizing code.")