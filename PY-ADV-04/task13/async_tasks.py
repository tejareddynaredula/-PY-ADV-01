import asyncio


async def process_data(item):
    print(f"Starting: {item}")
    await asyncio.sleep(2)
    print(f"Completed: {item}")
    return f"{item} processed"


async def main():
    print("=== PY-ADV-04 Task 13: Asynchronous Tasks ===")

    task1 = asyncio.create_task(process_data("Data 1"))
    task2 = asyncio.create_task(process_data("Data 2"))
    task3 = asyncio.create_task(process_data("Data 3"))

    results = await asyncio.gather(task1, task2, task3)

    print("\nResults:")
    for result in results:
        print(result)

    print("\nAll asynchronous tasks completed.")


if __name__ == "__main__":
    asyncio.run(main())