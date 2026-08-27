import asyncio
import time


def synchronous_task(task_name):
    print(f"Starting: {task_name}")
    time.sleep(2)
    print(f"Completed: {task_name}")


async def asynchronous_task(task_name):
    print(f"Starting: {task_name}")
    await asyncio.sleep(2)
    print(f"Completed: {task_name}")


def run_synchronous():
    print("\n=== Synchronous Execution ===")

    start = time.perf_counter()

    for task_name in ["Task 1", "Task 2", "Task 3"]:
        synchronous_task(task_name)

    return time.perf_counter() - start


async def run_asynchronous():
    print("\n=== Asynchronous Execution ===")

    start = time.perf_counter()

    tasks = [
        asyncio.create_task(asynchronous_task("Task 1")),
        asyncio.create_task(asynchronous_task("Task 2")),
        asyncio.create_task(asynchronous_task("Task 3"))
    ]

    await asyncio.gather(*tasks)

    return time.perf_counter() - start


if __name__ == "__main__":
    print("=== PY-ADV-04 Task 14 ===")
    print("Synchronous vs Asynchronous Execution")

    sync_time = run_synchronous()
    async_time = asyncio.run(run_asynchronous())

    print("\n=== Comparison ===")
    print(f"Synchronous execution time: {sync_time:.2f} seconds")
    print(f"Asynchronous execution time: {async_time:.2f} seconds")

    print("\nSynchronous execution runs tasks one after another.")
    print("Asynchronous execution allows waiting tasks to run concurrently.")