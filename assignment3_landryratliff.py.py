#DTSC 3020 – Assignment 3
# This exercise focuses on **if statements and conditional logic** in Python and is designed to help students practice decision-making structures.
# 
# **Total points:** 5  
# **Deadline:** Friday at midnight  
# **Submission:** Upload your Python file to your GitHub repository and submit **only your GitHub link**.
#
# ### Expectations
# - Write complete answers and run all cells before submission.
# - Keep the notebook clean (no unnecessary code).

### Question 1 – Movie Ticket System
# Write a Python code that checks the price of a movie ticket.
# If the age is between 0 and 11 it is Child, if between 12 and 17 it is Teen, and if 18 or older it is Adult.
# Print the category and the ticket price (you choose the price).
# Run the program with age = 16.
# write your answer here
age = 16
person = "Baby"
ticket = 0

if 0 <= age <= 11:
    person = "Child"
    ticket = 10
elif 12 <= age <= 17:
    person = "Teen"
    ticket = 20
elif age >= 18:
    person = "Adult"
    ticket = 25

print(f"{person}: ${ticket}")

### Question 2 – Online Store Discount
# Write a Python code that applies a discount based on the shopping cart total.
# If the total is less than 50 dollars there is no discount, if the total is between 50 and 99 dollars there is a 10 percent discount, and if the total is 100 dollars or more there is a 20 percent discount.
# Print the original total, the discount, and the final price.
# Run the program with cart_total = 85.
# write your answer here

cart_total = 85
discount = 0

if cart_total < 50:
    discount = 0
elif 50 <= cart_total < 100:
    discount = 10
elif cart_total >= 100:
    discount = 20

#:.2f formats the numbers to two decimal places
print(f"Original Total: ${cart_total:.2f}")
print(f"Discount: {discount:.2f}%")
print(f"Final Total: ${cart_total - (cart_total * discount/100):.2f}")


### Question 3 – Exam Grading
# Write a Python code that gives a letter grade for a score.
# If the score is between 90 and 100 the grade is A, if between 80 and 89 the grade is B, if between 70 and 79 the grade is C, if between 60 and 69 the grade is D, and if below 60 the grade is F.
# Print the grade and a short message.
# Run the program with score = 73.
# write your answer here

grade = 73

if grade < 60:
    grade = "F"
elif 60 <= grade < 70:
    grade = "D"
elif 70 <= grade < 80:
    grade = "C"
elif 80 <= grade < 90:
    grade = "B"
elif 90 <= grade <= 100:
    grade = "A"
else:
    grade = "A"


print(f"You got an {grade} in the class!")

### Question 4 – Parking Fee
# Write a Python code that calculates parking fees.
# If the car is parked for 0 to 2 hours the parking is free, if the car is parked for 3 to 5 hours the fee is 3 dollars per hour, and if the car is parked for more than 5 hours the fee is 3 dollars per hour for the first three hours after free and then 5 dollars per hour for the rest.
# Print the number of hours and the total fee.
# Run the program with hours = 6.
# write your answer here

hours = 6
total_fee = 0

if 0 <= hours <= 2:
    total_fee = 0
elif 3 <= hours <= 5:
    total_fee = 3 * (hours - 2) #free hours
elif hours > 5:
    total_fee = 5 * (hours - 5) + 9 #free hours

print(f"Total Hours: {hours} hrs")
print(f"Total Fee: ${total_fee}")

### Question 5 – Cafeteria Menu
# Write a Python code that creates a list with three food items.
# Check if an order is in the list.
# If the item is in the list print a confirmation, and if the item is not in the list print a polite message.
# Run the program with menu = ['pizza','salad','sandwich'] and order = 'salad'.
# write your answer here

order = 'salad'
menu = ['pizza', 'salad', 'sandwich']

if order in menu:
    print(f"{order.title()} is on the menu.")
else:
    print(f"{order.title()} is not on the menu.")

### Question 6 – Job Application Filter
# Write a Python code that checks if a person is eligible for a job.
# If the person is older than 22 and has more than 2 years of experience print Accepted.
# Otherwise, print Not Accepted.
# Run the program with age = 23 and experience = 1.
# write your answer here

age = 23
experience = 1

if (age > 22) and (experience > 2):
    print("Accepted")
else:
    print("Not Accepted")

### Question 7 – Clothing Advice
# Write a Python code that suggests clothing based on the temperature.
# If the temperature is below 10 print Coat and gloves, if the temperature is between 10 and 19 print Jacket, and if the temperature is 20 or more print T-shirt.
# Run the program with temperature = 15.
# write your answer here

temperature = 15

if temperature < 10:
    print("Coat and gloves")
elif 10 <= temperature < 20:
    print("Jacket")
elif temperature >= 20:
    print("T-shirt")

### Question 8 – Loan Eligibility
# Write a Python code that checks loan eligibility.
# If the salary is at least 3000 and the credit score is at least 650 print Loan Approved, otherwise print Loan Denied.
# Run the program with salary = 3500 and credit_score = 640.
# write your answer here

salary = 3500
credit_score = 640

if (salary >= 3000) and (credit_score >= 650):
    print("Loan Approved")
else:
    print("Loan Denied")

### Question 9 – Password Strength
# Write a Python code that checks if a password is strong, medium, or weak based on its length.
# If the password has fewer than 6 characters it is Weak, if it has 6 to 10 characters it is Medium, and if it has more than 10 characters it is Strong.
# Print the strength.
# Run the program with password = 'hello123'.
# write your answer here

password = 'hello123'

count = len(password)

if count < 6:
    print("Weak Password")
elif 6 <= count <= 10:
    print("Medium Password")
elif count > 10:
    print("Strong Password")

### Question 10 – Guest List Checker
# Write a Python code that creates a list with three invited guests.
# Define a variable for a guest name.
# Check if the guest name is in the list.
# If the guest is in the list print Welcome, and if the guest is not in the list print Not on the list.
# Run the program with guest = 'Sara'.
# write your answer here

guest = 'Sara'
x = ['Landry', 'Aspen', 'Bennett']

if guest in x:
    print(f"Welcome {guest}!")
else:
    print(f"{guest} not on the list!")
