#DTSC 3020 — Midterm Exam (Part 2: Programming)
#University of North Texas
#Course: Introduction to Computation with Python (DTSC 3020)
#Exam: Midterm — Programming (Ch. 1–8 concepts)

#Question 1 — Create Member ID
#Write a Python function create_member_id(full_name) that creates a Library Member ID from a person’s full name.
#Rules
#Normalize the name: remove extra spaces, convert to lowercase, and split by spaces.
#Use the last word as the last name (e.g., "John Ronald Reuel Tolkien" → last name tolkien).
#Use the first letters of all earlier words as initials (e.g., jrr for the example above).
#Construct the member ID in this exact format: lastname_initials (underscore between them; no spaces).
#Part 2 — Test Scenario (run using your function) names = ["Sara Amini", "Ali", "Mary Jane", "John Smith", "LINA", "madonna", "sara amini"]

full_name = ["Sara Amini", "Ali", "Mary Jane", "John Smith", "LINA", "madonna", "sara amini", "John Ronald Reuel Tolkien"]
print(full_name)

def create_member_id(full_name):
    member_id = []  #List to store generated member_id

    for name in full_name:
        name = name.strip().lower()  #name Remove extra spaces and convert to lowercase
        x = name.count(' ')          #Count how many spaces
        first = ''                   #First name
        last = ''                    #Last name

        if x == 0:                  #One name
            first = name[0]         #Takes index 0 of first name
            last = name
        else:                       #Two or more names
            for i in range(x):
                first = first + name.split(' ')[i][0]  #Makes a string and adds first letter of each name
            last = name.split(' ')[x]                  #Last name

        #Create member_id; prints last_first
        member_id.append(f'{last}_{first}')

    #Print all generated member_id's
    for id in member_id:
        print(id)

    return member_id

create_member_id(full_name)

#Question 2 — Movie Ticket Booth
#Write a Python program that simulates a movie ticket booth using this price list:
#prices = {"adult": 12.5, "child": 8, "senior": 9.5, "student": 10}
#Program Requirements
#Repeatedly ask the user to enter a ticket type or type done to finish.
#Valid inputs: adult, child, senior, student, or done.
#If the ticket type exists, add its price to a running total and print a confirmation message.
#If it doesn’t exist, print "Invalid ticket type".
#When the user types done, stop and show:
#Subtotal (sum of valid ticket prices)
#Tax = 8% of subtotal
#Final total = subtotal + tax
#Part 2 — Example Scenario When prompted, type the following (each on a new line), then press Enter after each entry:
#adult
#child
#student
#done

prices = {"adult": 12.5, "child": 8, "senior": 9.5, "student": 10}
total = 0.0

while True:
    ticket = input("Enter ticket type (adult, child, senior, student) or 'done' to finish: ").lower()

    if ticket == "done":
        break
    elif ticket in prices:
        total = total + prices[ticket]
        print(f"Added {ticket} ticket: ${prices[ticket]:.2f}")
    else:
        print("Invalid ticket type")

#Calculate totals
tax = total * 0.08
final_total = total + tax

print("\n--- Receipt ---")
print(f"Subtotal: ${total:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Final Total: ${final_total:.2f}")

#Question 3 — Student Grade Analyzer
#Write a Python function analyze_grades(grades) that takes a list of numbers (0–100) and returns three values:
#average grade
#highest grade
#lowest grade
#Constraints
#Use a function and return statement(s).
#Do not use external libraries.
#Part 2 — Test Scenario
#sample = [88, 92, 79, 93, 85, 90, 72]

def analyze_grades(grades):
    average = sum(grades)/len(grades)
    highest = max(grades)
    lowest = min(grades)
    return average, highest, lowest

# Test Scenario
sample = [88, 92, 79, 93, 85, 90, 72]

avg, high, low = analyze_grades(sample)

print(f"Average grade: {avg:.2f}")
print(f"Highest grade: {high}")
print(f"Lowest grade: {low}")

#Question 4 — PIN Verification
#Write a Python program that simulates an ATM PIN verification system.
#Requirements
#The correct PIN is 4321.
#The user has at most 3 attempts to enter the correct PIN.
#If the PIN is correct: print Access granted. and stop.
#If all 3 attempts fail: print Card blocked.
#After each wrong attempt, also print the counter in the form Wrong (x/3).
#Part 2 — Test Scenario Run your program and, when prompted, enter these sequences to verify both behaviors:
#Scenario A
#1111
#2222
#4321

x = 0

while x < 3:
    pin = input("Enter your PIN (4 digit number): ")
    if pin == "4321":
        print("Access granted.")
        break
    else:
        x = x + 1
        print(f"Wrong ({x}/{3})")
else:
    print("Card blocked.")



































