age = 19

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Elder")

miles = 5200

if miles < 3000:
    print("Oil is fine.")
elif miles < 5000:
    print("Consider changing soon.")
else:
    print("Oil change needed!")

age = 20
if age < 13:
    print("Too young.")
elif age < 18:
    print("You can play with parental guidance.")
else:
    print("You can play freely!")

score = 5

if score < 3:
    print("Beginner")
elif score < 5:
    print("Intermediate")
elif score < 7:
    print("Pro")
else:
    print("Legend")

zones = 3

if zones == 1:
    print("$2.50")
elif zones <= 3:
    print("$3.25")
else:
    print("$4.00")

pantry = ["rice", "pasta", "flour"]

if "milk" not in pantry:
    print("Add milk to shopping list")

if "eggs" not in pantry:
    print("Add eggs to shopping list")

post = "Check this amazing offer, no clickbait here!"

banned_word_1 = "spam"
banned_word_2 = "clickbait"

if (banned_word_1 in post.lower()) or (banned_word_2 in post.lower()) or (len(post) >= 140):
    print("Send to review")
else:
    print("OK to publish")

score = 19

if score < 20:
    print("Locked! You need at least 20 points to play.")
elif score < 50:
    print("Welcome to Level 1!")
elif score < 80:
    print("Welcome to Level 2!")
else:
    print("Welcome to Level 3 — Expert mode!")

#Write your answer here, upload this file to your gitHub repository and send me the link in Canvas messages.
cart = ['bread', 'milk', 'eggs', 'rice']

if 'bread' in cart and 'milk' in cart:
    print("Free butter included!")

if 'eggs' in cart or 'rice' in cart:
    print("Free spoon included!")

gift = False

if 'bread' in cart:
    gift = True
elif 'milk' in cart:
    gift = True
elif 'eggs' in cart:
    gift = True
elif 'rice' in cart:
    gift = True

if not gift:
    print("No free gift")

if not gift:
    print("No free gift")


