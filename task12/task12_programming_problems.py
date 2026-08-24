# PY-ADV-01 - Task 12
# Python Programming Problems


print("=== 1. Reverse a String ===")

text = "Python"

reversed_text = text[::-1]

print("Original:", text)
print("Reversed:", reversed_text)


print("\n=== 2. Check Palindrome ===")

word = "madam"

if word == word[::-1]:
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")


print("\n=== 3. Factorial of a Number ===")

number = 5
factorial = 1

for value in range(1, number + 1):
    factorial *= value

print("Number:", number)
print("Factorial:", factorial)


print("\n=== 4. Find Largest Number ===")

numbers = [10, 25, 7, 42, 18]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Numbers:", numbers)
print("Largest:", largest)


print("\n=== 5. Count Vowels ===")

text = "Python Programming"

vowels = "aeiouAEIOU"

vowel_count = 0

for character in text:
    if character in vowels:
        vowel_count += 1

print("Text:", text)
print("Number of vowels:", vowel_count)


print("\n=== 6. Remove Duplicates ===")

numbers = [1, 2, 2, 3, 4, 4, 5, 5]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("Original:", numbers)
print("Without duplicates:", unique_numbers)


print("\n=== 7. Find Second Largest Number ===")

numbers = [10, 20, 40, 30, 50]

unique_numbers = list(set(numbers))
unique_numbers.sort()

second_largest = unique_numbers[-2]

print("Numbers:", numbers)
print("Second largest:", second_largest)


print("\n=== 8. Check Prime Number ===")

number = 17

is_prime = True

if number < 2:
    is_prime = False
else:
    for value in range(2, int(number ** 0.5) + 1):
        if number % value == 0:
            is_prime = False
            break

if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")


print("\n=== 9. Fibonacci Series ===")

terms = 10

first = 0
second = 1

fibonacci = []

for _ in range(terms):
    fibonacci.append(first)
    first, second = second, first + second

print("Fibonacci series:", fibonacci)


print("\n=== 10. Word Frequency ===")

sentence = "python is easy and python is powerful"

words = sentence.split()

word_frequency = {}

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

print("Sentence:", sentence)
print("Word frequency:", word_frequency)


print("\n=== 11. Edge Cases ===")

# Empty string
empty_text = ""

print("Empty string reverse:", empty_text[::-1])


# Empty list
empty_numbers = []

if empty_numbers:
    print("Largest:", max(empty_numbers))
else:
    print("Largest: No numbers available")


# Zero factorial
zero_factorial = 1

print("Factorial of 0:", zero_factorial)


# Prime edge case
number = 1

if number < 2:
    print("1 is not a prime number.")


print("\n=== 12. Mixed Input Handling ===")

mixed_values = [10, "20", 30, "40", 50]

numeric_values = []

for value in mixed_values:
    if isinstance(value, (int, float)):
        numeric_values.append(value)

print("Mixed values:", mixed_values)
print("Numeric values:", numeric_values)