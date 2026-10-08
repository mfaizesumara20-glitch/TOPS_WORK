"""
Task: Visualize Food Wastage in a Canteen Management System

Create a Python program using Pandas and Matplotlib to analyze and visualize food wastage in a canteen management system.

Requirements

Create a dataset containing:

Food item name

Quantity prepared (in kg)

Quantity consumed (in kg)

Quantity wasted (in kg)

Create a Pandas DataFrame from the dataset.

Calculate the total food wastage for each food item.

Use a pie chart to visualize the percentage of total food wastage contributed by each food item.

Display:

Food item names as labels

Wasted quantity as the pie-chart values

Percentage of wastage on each slice

A suitable chart title such as "Canteen Food Wastage Analysis"

Display the DataFrame before displaying the chart.

Expected Output

The program should display a table containing the canteen food-wastage data and a pie chart showing the proportion of total wastage for each food item.

Example Food Items

Rice

Dal

Vegetables

Chapati

Curry

Salad

The objective is to help canteen management identify which food items contribute most to overall food wastage.


"""


# import pandas as pd
# import matplotlib.pyplot as plt



# data={
#     "food item": ["Rice","Dal","Vegetables","Chpati","Curry","Salad"],
#     "quantity_prepard" : [50,20,26,10,15,60],
#     "quantity_consumed" :[42,16,20,9,12,50],
#     "quantity_wasted" : [8,4,6,1,3,10]


# }

# df=pd.DataFrame(data)
# print(df)

# total_food_watage=df["quantity_wasted"].sum()


# plt.pie(df["total_food_watage"], labels=df["food item"],autopct="%1.1f%%")
# plt.title("Food wastage")
# plt.show()




import pandas as pd
import matplotlib.pyplot as plt

data = {
    "food item": ["Rice", "Dal", "Vegetables", "Chapati", "Curry", "Salad"],

    "quantity_prepard": [50, 20, 26, 10, 15, 60],

    "quantity_consumed": [42, 16, 20, 9, 12, 50],

    "quantity_wasted": [8, 4, 6, 1, 3, 10]
}

df = pd.DataFrame(data)

print(df)

total_food_watage = df["quantity_wasted"].sum()

print("Total food wastage:", total_food_watage)

plt.pie(
    df["quantity_wasted"],
    labels=df["food item"],
    autopct="%1.1f%%"
)

plt.title("Food Wastage")

plt.show()