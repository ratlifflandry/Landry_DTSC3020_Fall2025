#DTSC 3020 – Assignment 4
#Chapter 6 – Dictionaries
#Total points: 4
#Deadline: Friday at midnight
#Submission: Upload your Python file to your GitHub repository and submit only your GitHub link.
#Expectations Write complete answers and run all cells before submission. Keep the notebook clean (no unnecessary code).

#Exercise 1: Find and print the student with the lowest grade.
grades = {
    'Ali': 17,
    'Sara': 19,
    'Reza': 18.5,
    'Lina': 20,
    'Omid': 16
}
#Write your code here:
name = 0
score = min(grades.values())

for key, value in grades.items():
    if value == score:
        print(key)

#Exercise 2: print names of students who registered for any course containing "Data"
courses = {
    'Ali': ['Python', 'Math'],
    'Sara': ['Data Mining', 'Chemistry'],
    'Reza': ['Machine Learning', 'Data Science'],
    'Lina': ['English', 'History']
}
#Write your code here:
for key, value in courses.items():
    for course in value:
        if 'Data' in course:
            print(key)

#Exercise 3: Print titles of books that are not available.
library = {
    'Python101': {'pages': 180, 'available': True},
    'AI Basics': {'pages': 130, 'available': False},
    'Math Advanced': {'pages': 200, 'available': False},
    'Statistics': {'pages': 175, 'available': True}
}
#Write your code here:
for key, value in library.items():
    if value['available'] == False:
        print(key)

#Exercise 4: Print names of students who are registered for more than 2 courses.
registrations = {
    'Ali': ['Python', 'Math'],
    'Sara': ['Biology', 'Chemistry', 'Math'],
    'Reza': ['English'],
    'Lina': ['History', 'Physics', 'Geography', 'Art']
}
#Write your code here:
for key, value in registrations.items():
    if len(value) > 2:
        print(key)

#Exercise 5: Calculate and print the average grade of the class.
grades = {
    'Ali': 17,
    'Sara': 19,
    'Reza': 18.5,
    'Lina': 20,
    'Omid': 16
}
#Write your code here:
total_score = 0
count = len(grades)

for key, value in grades.items():
    total_score = total_score + value

average = total_score/count
print(average)

#Exercise 6: Count and print the number of students registered for "Python."
courses = {
    'Ali': ['Python', 'Math'],
    'Sara': ['Biology', 'Chemistry'],
    'Reza': ['Python', 'AI'],
    'Lina': ['English', 'History'],
    'Omid': ['Python']
}
#Write your code here:
count = 0

for key, value in courses.items():
    if 'Python' in value:
        count = count + 1

print(count)

#Exercise 7: Print titles of books with more than 200 pages.
book_pages = {
    'Python101': 180,
    'AI Basics': 230,
    'Math Advanced': 250,
    'Statistics': 190,
    'Data Science': 300
}
#Write your answer here
for key, value in book_pages.items():
    if value > 200:
        print(key)

#Exercise 8: Print each student's name and number of registered courses.
courses = {
    'Ali': ['Python', 'Math'],
    'Sara': ['Biology', 'Chemistry'],
    'Reza': ['Python', 'AI'],
    'Lina': ['English', 'History'],
    'Omid': ['Python']
}
#Write your code here:
for key, value in courses.items():
    print(f"{key}: {len(value)}")