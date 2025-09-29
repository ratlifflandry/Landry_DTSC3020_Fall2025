#Write a Python program that simulates a self-checkout system.**
#Use this price list: prices: apple= 1 , bread= 2.5 , milk=5 , egg= 6
#Program requirements:
#The program should repeatedly ask the user to enter an item name or enter "pay".
#Valid inputs are the names of the **items above ** or the word "pay".
#If the entered item exists in the price list:
#Add its price to the running total.
#Print the message: "Added , running total: $".
#If the entered item does not exist in the price list:
#Print "Item not found".
#If the user types "pay":
#Stop asking for input.
#Show the following three values:
#Subtotal: the sum of all valid items entered.
#Tax: 8% of the subtotal. (0.08 * total)
#Final total: subtotal + tax.
#Run your program with this purchase list. For example, for one person whose purchase is:apple, pizza, bread, pay italicised text

#Self-checkout system
prices = {
    "apple": 1.0,
    "bread": 2.5,
    "milk": 5.0,
    "egg": 6.0
}
subtotal = 0.0

print("Welcome to the self-checkout! Type item names to add them, or 'pay' to finish.")

while True:
    item = input("Enter item (or 'pay' to finish): ").lower().strip()

    if item == "pay":
        break
    elif item in prices:
        subtotal += prices[item]
        print(f"Added {item}, running total: ${subtotal:.2f}")
    else:
        print("Item not found")

tax = subtotal * 0.08
final_total = subtotal + tax

print("\n--- Receipt ---")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Final total: ${final_total:.2f}")
