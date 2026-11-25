# import matplotlib.pyplot as plt
# import pandas as pd
# from matplotlib.animation import FuncAnimation
# import random 
# data = {
#     "food item": ["Rice", "Dal", "Vegetables", "Chapati", "Curry", "Salad"],
#     "wastage": [10, 50, 20, 30, 40, 60]
# }

# # data set of food wastage
# df = pd.DataFrame(data)
# print(df)


# # create a figure
# ax = plt.figure(figsize=(5, 5))

# # create a function for updating the chart

# def update(frame):
#     # cleare the old chart
#     ax.clear()

#     # ganratte a new random wastage data
#     df["wastage"] =[

#         random.randint(0,20),
#         random.randint(0,30),
#         random.randint(0,40),
#         random.randint(0,20),
#         random.randint(0,10),
#         random.randint(0,70)
#     ]
# # ceate a chart using the new data
# plt.pie(
#     df["wastage"],
#     labels=df["food item"],
#     autopct="%1.1f%%"
#  )
# ax.set_title("Food Wastage")

# # apply animation to the chart
# ani = FuncAnimation(ax, update, interval=1000, cache_frame_data=False)

# plt.show()



import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

data = {
    "food item": ["Rice", "Dal", "Vegetables", "Chapati", "Curry", "Salad"],
    "wastage": [10, 50, 20, 30, 40, 60],
}

df = pd.DataFrame(data)
print(df)

# Create both Figure and Axes
fig, ax = plt.subplots(figsize=(5, 5))


def update(frame):
    ax.clear()

    # Properly indented inside update(); avoid all-zero sums
    df["wastage"] = [
        random.randint(0, 20),
        random.randint(0, 30),
        random.randint(0, 40),
        random.randint(0, 20),
        random.randint(0, 10),
        random.randint(0, 70),
    ]

    

    ax.pie(
        df["wastage"],
        labels=df["food item"],
        autopct="%1.1f%%",
    )
    ax.set_title("Food Wastage")


# Pass `fig` (the Figure) to FuncAnimation
ani = FuncAnimation(fig, update, interval=1000, cache_frame_data=False)

plt.show()