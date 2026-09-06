# Create a class called FoodOrder with attributes: restaurant_name, items (list), and total_price. Write an __init__() constructor to initialize these, then create an object representing your last Zomato or Swiggy order and print its details.


class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price


order1 = FoodOrder(
    "Zomato Restaurant",
    ["Pizza", "Burger"],
    450
)

print("Restaurant:", order1.restaurant_name)
print("Items:", order1.items)
print("Total Price:", order1.total_price)