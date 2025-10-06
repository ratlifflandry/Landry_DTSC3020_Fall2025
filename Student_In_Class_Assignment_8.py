#Write a Python function create_email(full_name) that builds a UNT email in the format firstname.lastname@my.unt.edu.
#Rules
#Use the first and last word from full_name (case-insensitive).
#Convert everything to lowercase.
#If there is only one word, use it twice (e.g., "ali" → ali.ali@my.unt.edu).
#Return the email string.

#Constraints
#Use a function and return.
#Do not use input() or external libraries.
#test your code with this list names = [ "Sara Amini", "Ali", "Mary Jane", " John Smith ", "LINA", "madonna", " sara amini "]

def create_email(full_name):

    full_name = full_name.strip()
    parts = full_name.split()

    #Change all words to lowercase
    for i in range(len(parts)):
        parts[i] = parts[i].lower()

    #Use same first name for last name
    if len(parts) == 1:
        first = parts[0]
        last = parts[0]
    else:
        first = parts[0]
        last = parts[-1]

    #Email
    email = first + "." + last + "@my.unt.edu"
    return email

#Function
names = ["Sara Amini", "Ali", "Mary Jane", " John Smith ", "LINA", "madonna", " sara amini "]

for name in names:
    print(f"{name} -> {create_email(name)}")