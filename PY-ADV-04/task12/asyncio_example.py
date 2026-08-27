import asyncio


async def process_data(item):
    print(f"Processing {item}...")
    await asyncio.sleep(1)
    print(f"Completed {item}")


async def main():
    print("=== PY-ADV-04 Task 12: Asyncio ===")

    await process_data("Data 1")
    await process_data("Data 2")
    await process_data("Data 3")

    print("\nAsynchronous processing completed.")


if __name__ == "__main__":
    asyncio.run(main())