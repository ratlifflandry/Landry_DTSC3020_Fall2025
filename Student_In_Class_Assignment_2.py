#### ✅ Final Class Exercise: Library Borrowing (using key-value)
# You are given a dictionary that shows how many books each student has borrowed. Write a Python program to:
# 1. Print the names of students who borrowed more than 2 books.
# 2. Calculate the total number of borrowed books.

borrowed_books = {
    'Ali': 1,
    'Sara': 3,
    'Reza': 0,
    'Lina': 4,
    'Omid': 2
}

#write your answer here part 1
for key, value in borrowed_books.items():
    if value > 2:
        print(f"{key}: {value}")

#write your answer here part 2
x = 0
for key, value in borrowed_books.items():
    x = x + value

print(f"Total Number of Borrowed Books: {x}")



