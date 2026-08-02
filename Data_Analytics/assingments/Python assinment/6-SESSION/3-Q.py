food_prices = {
    'Margherita Pizza' : [250],
    'Chicken Biryani' : [350],
    'Veg Hakka Noodles' : [180],
    'Grilled Chicken Burger' : [220],
    'Paneer Butter Masala' : [450]

}

for food, cost in food_prices.items():
    if cost > [200]:
        print(food, ':' , cost)


