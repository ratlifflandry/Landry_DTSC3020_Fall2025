import pandas as pd
import math
import statistics
import matplotlib.pyplot as plt
import numpy as np
import random

#Print Hello World
print("Hello World!")

#Variables
x = 1                               #Integer
y = 3.14                            #Float
name = "Adam"                       #String
car = True                          #Boolean
list = [1, 2, 3]                    #List
set = {1, 2, 3}                     #Set
dictionary = {1:'a', 2:'b', 3:'c'}  #Dictionary
complex = 1j + 1                    #Complex number

#Print Variables
print(x, y, name, car, list, set, dictionary, complex)

#Draw a Square
for i in range(4):
    print("0" * 10)

#Draw a Triangle
for i in range(1, 6):
    x = " " * (5 - i) + "0" * i
    y = "0" * i
    print(x + y)

#Draw a Circle
r = 25

for y in range(-r, r + 1):
    for x in range(int(-r * 2.5), int(r * 2.5) + 1):
        d = math.sqrt((x/2.5)**2 + y**2)
        if d <= r:
            print("O", end="")
        else:
            print(" ", end="")
    print()

#Printing ASCII Code
code = []
for i in range(0, 256):
    code.append(chr(i))
print(code)

#Casting Variables
print(int(5.0))             #Integer
print(float(5))             #Float
print("Pi = " + str(3.14))  #String
print(bool(1))              #Boolean
print(chr(1))               #Character

#if statement
print("Guess what number I'm thinking of?")
a = int(input("Enter number: "))
if a == 1:
    print("You guessed correctly!")
elif a != 1:
    print("You guessed incorrectly!")

#Example of 'and' statement
age = 25
license = True

if age >= 16 and license:
    print("You are allowed to drive.")
else:
    print("You are not allowed to drive.")

#Example of 'or' statement
rainjacket = True
umbrella = False

if rainjacket or umbrella:
    print("You can go outside.")
else:
    print("You should stay inside.")

#Creating a list
numbers = [1,2,3,4,5,6,7,8,9, 10]
print(numbers)

#Creating a list
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black", "white", "brown", "gray"]
print(colors)

#Count number of items in list
count = 0
for i in colors:
    count = count + 1

print("Number of items: " + str(count))

#print using array index
print(colors[4], colors[6], colors[7])

#Loop through colors
for i in colors:
    print(i)

#Add + Remove elements
colors.append("baby blue")
colors.remove("red")

#Creating a set
set1 = {0, 1, 2}
set2 = {1, 2, 3, 4, 5}
print(set1)
print(set2)

#Intersection + Union
union = set1.union(set2)
intersection = set1.intersection(set2)
print(union)
print(intersection)

#Add + Remove elements
set1.add(3)
set1.remove(0)

#Creating a dictionary
person = {"name": "Landry", "age": 21, "birthday": "03/30/2004"}
print(person["name"])
print(person["age"])
print(person["birthday"])

#Add + Remove
person["city"] = "Mckinney, TX"
del person["age"]
print(person)

#For loop
for i in range(10):
    print(i)  #Outputs: 0 1 2 3 4 5 6 7 8 9

#For loop start/stop
for i in range(0, 101, 5):
    print(i) #Outputs: 0 5 10, . . ., 100

#While loop
count = 0
while count < 10:
    print(count) #Outputs: 0 1 2 3 4 5 6 7 8 9
    count = count + 1

#While loop choices
while True:
    choice = input("Choose between door 1, 2, or 3:")

    if choice == '1':
        print("You win a million dollars: $1,000,000")
        break

    elif choice == '2':
        print("You win a Ferrari LaFerrari!")
        break

    elif choice == '3':
        print("You died!")
        break

#If-else statement
x = 1
if x == 1:
    print("True")
else:
    print("False")

#Try-except block
try:
    x = 1 / 0
except:
    print("Error")

#Returns an integer between 1 and 10
random_integer = random.randint(0, 10)
print("Random Integer: " + str(random_integer))

#Returns a float between 0 and 10
random_float = random.uniform(0, 10)
print("Random Decimal: " + str(random_float))

#Returns a character A-Z
list1 = []

for i in range(65, 91):
    list1.append(chr(i))

for i in range(97, 123):
    list1.append(chr(i))

i = random.randint(0, 51)
print("Random Character: " + list1[i])

#Returns an element from list
my_list = ['a', 'b', 'c', 1, 2, 3]
random_choice = random.choice(my_list)
print("Random Choice: " + str(random_choice))

#Mean, Max, Min, Median, Mode
list10 = [1,2,3,4,5,6,7,8,9,10,5,5,5,5,5,3.14]

print("List: " + str(list10))
print("Mean: " + str(statistics.mean(list10)))
print("Max: " + str(max(list10)))
print("Min: " + str(min(list10)))
print("Median: " + str(statistics.median(list10)))
print("Mode: " + str(statistics.mode(list10)))
print("Standard Deviation: " + str(statistics.stdev(list10)))

#Total, Count, Mean, Max, Min of dataset
count = 0
total = 0
x = list10[0]
y = list10[0]

for i in list10:
    count = count + 1
    total = i + total

    if i > x:
        x = i

    if i < y:
        y = i

print("Total: " + str(total))
print("Count: " + str(count))
print("Mean: " + str(total/count))
print("Max: " + str(x))
print("Min: " + str(y))

#Sort List
sorted_list = sorted(list10)
print("Sorted List: " + str(sorted_list))

#Bubble Sort for Data
def bubble_sort(List):

#Length of the list
    count = 0
    for i in List:
        count = count + 1

    sort = False

    while not sort:
        sort = True
        for i in range(0, count - 1):
            if List[i] > List[i + 1]:  #Swap if out of order
                sort = False
                x = List[i]
                List[i] = List[i + 1]
                List[i + 1] = x
    return List

#Bubble Sort
print("Bubble Sort: " + str(bubble_sort(list10)))

#Copy list
copy_list = []

for i in range(0, count):
    copy_list.append(list10[i])

print("Copy List: " + str(copy_list))

#Defining a function
def greet(name):
    return "Hello " + name + "!"

#Calling a function
print(greet("John")) # Outputs: Hello John!

#Define a class
class Person:
    #Constructor to initialize name + age
    def __init__(self, name, age):
        #Instance variable name + age
        self.name = name
        self.age = age

    #Method to greet name
    def greetname(self):
        return "Hello, my name is " + str(self.name) + "."

    #Method to greet age
    def greetage(self):
        return "I am " + str(self.age) + " years old."

#Creating an object
p0 = Person("John", 25)
print(p0.greetname())   #Outputs: Hello, my name is John.
print(p0.greetage())    #Outputs: I am 25 years old.

#Define a class Circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return math.pi * self.radius ** 2

    def Circumference(self):
        return 2 * math.pi * self.radius

#Circle Object
radius = 5
p1 = Circle(radius)
print("Radius = " + str(radius))
print("Area = " + str(p1.Area()))
print("Circumference = " + str(p1.Circumference()))

#Define a class Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Area(self):
        return self.length * self.width

    def Perimeter(self):
        return 2 * self.length + 2 * self.width

#Rectangle Object
length = 5
width = 5
p2 = Rectangle(length, width)
print("Length = " + str(length))
print("Width = " + str(width))
print("Area = " + str(p2.Area()))
print("Perimeter = " + str(p2.Perimeter()))

#Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello World! 12345")

#Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  #Outputs: Hello, World!

#Counting letters in a string
text = "abcdefghijklmnopqrstuvwxyz"
count = text.count('a')
print("# of a = " + str(count))