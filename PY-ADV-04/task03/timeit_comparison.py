import timeit


def calculate():
    total = 0

    for number in range(10000):
        total += number

    return total


execution_time = timeit.timeit(
    calculate,
    number=1000
)

print("=== PY-ADV-04 Task 3: Using timeit ===")
print(f"Execution time: {execution_time:.6f} seconds")
print("Number of executions: 1000")
print("timeit was used successfully to measure execution time.")