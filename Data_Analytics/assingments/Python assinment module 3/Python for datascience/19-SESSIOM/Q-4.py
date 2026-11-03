# Extend the FoodOrder class by adding a method add_item(self, item_name, item_price) that adds the item to the items list and updates total_price. Demonstrate by adding two items to your order and printing the updated total.



class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

    def add_item(self, item_name, item_price):
        self.items.append(item_name)
        self.total_price += item_price


order1 = FoodOrder(
    "Zomato Restaurant",
    ["Pizza"],
    300
)

print("Before adding:")
print("Items:", order1.items)
print("Total:", order1.total_price)

order1.add_item("Burger", 150)
order1.add_item("Fries", 100)

print("\nAfter adding:")
print("Items:", order1.items)
print("Total:", order1.total_price)

