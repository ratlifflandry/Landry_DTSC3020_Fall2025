# -------------------------------
# Exercise 1
# Create a list with 3 fruits (for example: apple, banana, orange).
# • Print the entire list.
# • Print each item separately.
fruits = ["apple", "banana", "orange"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])

# -------------------------------
# Exercise 2
# Create a list with 4 names.
# • Change the first name to a different one.
# • Print the new list.
names = ["Tom", "Cruise", "Landry", "Ratliff"]
names[0] = "Maverick"
print(names)

# -------------------------------
# Exercise 3
# Create a list with 5 vehicles (for example: car, bus, bike).
# • Add one more vehicle to the end of the list.
# • Print the list.
vehicles = ["car", "boat", "airplane", "spaceship", "motorcycle"]
vehicles.append("bus")
print(vehicles)

# -------------------------------
# Exercise 4
# Create a list with 6 foods.
# • Remove one food from the list.
# • Print the new list.
foods = ["pizza", "orange chicken", "fried rice", "cake", "cookie", "queso & chips"]
foods.remove("cake")
print(foods)

# -------------------------------
# Exercise 5
# Create a list with 4 cities.
# • Sort the list in alphabetical order.
# • Reverse the list.
cities = ["Dallas", "New York", "Los Angeles", "Honolulu"]
cities.sort()
cities.reverse()
print(cities)

# -------------------------------
# Exercise 6
# Create a list with 3 animals.
# • Use a for loop to print each animal.
animals = ["Dog", "Lion", "Cheetah"]
for animal in animals:
    print(animal)

# -------------------------------
# Exercise 7
# Create a list with numbers from 1 to 5.
# • Use a for loop to print each number multiplied by 2.

numbers = [1, 2, 3, 4, 5]
print(numbers)

for i in range(0, 5):
    number = numbers[i] * 2
    print(number)

# -------------------------------
# Exercise 8
# Create a list with 6 friends.
# • Print the first three friends.
# • Print the last three friends.
friends = ["James", "John", "William", "Mary", "Elizabeth", "Jennifer"]

for friend in friends[0:3]:
    print(friend)

for friend in friends[3:6]:
    print(friend)

# -------------------------------
# Exercise 9
# Use range() to create a list with numbers from 1 to 10.
# • Print the list.
count = []
for i in range(1, 11):
    count.append(i)

print(count)

# -------------------------------
# Exercise 10
# Use list comprehension to create a list with the squares of numbers from 1 to 5.
# • Print the list.
squares = [x ** 2 for x in range(1, 6)]
print(squares)
