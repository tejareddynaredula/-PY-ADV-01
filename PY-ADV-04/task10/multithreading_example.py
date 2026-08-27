import threading
import time


def download_file(file_name):
    print(f"Starting download: {file_name}")
    time.sleep(2)
    print(f"Completed download: {file_name}")


files = [
    "file1.txt",
    "file2.txt",
    "file3.txt"
]

print("=== PY-ADV-04 Task 10: Multithreading ===")

start_time = time.perf_counter()

threads = []

for file_name in files:
    thread = threading.Thread(
        target=download_file,
        args=(file_name,)
    )
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

execution_time = time.perf_counter() - start_time

print("\nAll threads completed.")
print(f"Total execution time: {execution_time:.2f} seconds")