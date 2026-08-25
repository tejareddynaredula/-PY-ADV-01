# PY-ADV-02 - Task 12
# Custom Context Manager


print("=== 1. Custom Context Manager ===")


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")
        if self.file:
            self.file.close()

        if exc_type:
            print("An exception occurred:", exc_value)

        return False


filename = "custom_data.txt"


print("\n=== 2. Writing Using Custom Context Manager ===")

with FileManager(filename, "w") as file:
    file.write("Name: Teja\n")
    file.write("Course: Python Backend\n")
    file.write("Task: Custom Context Manager\n")

print("Data written successfully.")


print("\n=== 3. Reading Using Custom Context Manager ===")

with FileManager(filename, "r") as file:
    content = file.read()

print("File Content:")
print(content)


print("=== 4. Automatic Resource Management ===")

with FileManager(filename, "r") as file:
    print("File is open inside the block:", not file.closed)

print("File was automatically closed after the block.")


print("\n=== 5. Exception Handling ===")

try:
    with FileManager(filename, "r") as file:
        print("Reading file safely...")
        raise ValueError("Simulated error inside context manager")
except ValueError as error:
    print("Handled exception:", error)


print("\n=== 6. Custom Context Manager Summary ===")

print("__enter__ -> Executes when entering the with block.")
print("__exit__  -> Executes when leaving the with block.")
print("Resources are automatically released.")
print("Exceptions can be handled during context cleanup.")