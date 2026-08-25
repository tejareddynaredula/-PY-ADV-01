class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __add__(self, other):
        return self.pages + other.pages


print("=== 1. Creating Book Objects ===")

book1 = Book("Python Basics", "Teja", 300)
book2 = Book("Advanced Python", "Sumanth", 400)
book3 = Book("Python Basics", "Teja", 300)

print("Books created successfully.")


print("\n=== 2. __str__ Method ===")

print(book1)


print("\n=== 3. __repr__ Method ===")

print(repr(book1))


print("\n=== 4. __len__ Method ===")

print("Pages in book1:", len(book1))


print("\n=== 5. __eq__ Method ===")

print("book1 == book2:", book1 == book2)
print("book1 == book3:", book1 == book3)


print("\n=== 6. __add__ Method ===")

total_pages = book1 + book2

print("Total pages of book1 and book2:", total_pages)


print("\n=== 7. Magic Methods Summary ===")

print("__init__  -> Initializes the object")
print("__str__   -> Controls user-friendly display")
print("__repr__  -> Controls developer representation")
print("__len__   -> Allows len() to be used")
print("__eq__    -> Allows objects to be compared")
print("__add__   -> Allows objects to be added")