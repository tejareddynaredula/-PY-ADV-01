import multiprocessing
import time


def cpu_intensive_task(number):
    total = 0

    for i in range(1, 1000000):
        total += (number * i) % 1000

    return total


if __name__ == "__main__":
    numbers = [1, 2, 3, 4]

    print("=== PY-ADV-04 Task 11: Multiprocessing ===")

    start_time = time.perf_counter()

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(cpu_intensive_task, numbers)

    execution_time = time.perf_counter() - start_time

    print("\nResults:")
    print(results)

    print(f"\nNumber of processes: 4")
    print(f"Total execution time: {execution_time:.2f} seconds")
    print("\nCPU-intensive work completed using multiprocessing.")