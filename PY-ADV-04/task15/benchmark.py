import asyncio
import multiprocessing
import threading
import time


def sync_task():
    for _ in range(3):
        time.sleep(1)


def thread_task():
    time.sleep(1)


async def async_task():
    await asyncio.sleep(1)


def run_threading():
    threads = []

    for _ in range(3):
        thread = threading.Thread(target=thread_task)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def run_multiprocessing():
    with multiprocessing.Pool(processes=3) as pool:
        pool.map(cpu_task, [1, 2, 3])


def cpu_task(number):
    total = 0

    for i in range(500000):
        total += (number * i) % 1000

    return total


async def run_async():
    tasks = [
        asyncio.create_task(async_task()),
        asyncio.create_task(async_task()),
        asyncio.create_task(async_task())
    ]

    await asyncio.gather(*tasks)


def benchmark(name, function):
    start = time.perf_counter()

    function()

    return time.perf_counter() - start


if __name__ == "__main__":
    print("=== PY-ADV-04 Task 15: Benchmark ===")

    sync_time = benchmark("Synchronous", sync_task)
    thread_time = benchmark("Multithreading", run_threading)
    process_time = benchmark("Multiprocessing", run_multiprocessing)

    start = time.perf_counter()
    asyncio.run(run_async())
    async_time = time.perf_counter() - start

    print("\n=== Benchmark Results ===")
    print(f"Synchronous:     {sync_time:.4f} seconds")
    print(f"Multithreading:  {thread_time:.4f} seconds")
    print(f"Multiprocessing: {process_time:.4f} seconds")
    print(f"Asyncio:         {async_time:.4f} seconds")

    print("\nBenchmark completed successfully.")