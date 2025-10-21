#create a class called InventoryItem that represents a single product in stock — for example, an apple in a grocery store. The class keeps track of the product’s name, price, quantity, and minimum stock level (the level where we might need to reorder).
class InventoryItem:
    def __init__(self, name, price, quantity = 0, min_stock = 0):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)
        self.min_stock = int(min_stock)

        if self.price < 0:
            raise ValueError("Price cannot be negative.")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if self.min_stock < 0:
            raise ValueError("Minimum stock level cannot be negative.")

    def restock(self, quantity):
        if quantity < 0:
            raise ValueError("Restock quantity cannot be negative.")
        self.quantity = self.quantity + quantity
        return self.quantity

    def sell(self, quantity):
        if quantity <= 0:
            raise ValueError("Sell quantity must be positive.")
        if self.quantity >= quantity:
            self.quantity = self.quantity - quantity
            return True
        else:
            return False

    def value(self):
        return self.price * self.quantity

    def __repr__(self):
        return (f"InventoryItem(name='{self.name}', price={self.price}, "
                f"quantity={self.quantity}, min_stock={self.min_stock})")

my_store = InventoryItem('Apple', 10, 5, 2)
print(my_store)

my_store.restock(10)
print(my_store.restock(25))
print(my_store.sell(3))
print(my_store.value())























