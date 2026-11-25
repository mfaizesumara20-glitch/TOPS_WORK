import matplotlib.pyplot as plt
import pandas as pd
# create a dataframes using pandas to plot data on chart

data = {

    "food": ["Rice", "Dal", "Vegetables", "Chapati", "Curry", "Salad"],
    "wastage": [10,50, 20, 30, 40, 60]
}

# dataframe

df = pd.DataFrame(data)
print(df)

#charts 
# craete a bar chart using matplotlib

plt.figure(figsize=(5, 5))
plt.bar(df["food"], df["wastage"], color=["green", "red", "blue", "yellow", "orange", "purple"])
plt.title("Food Wastage in Canteen")
plt.xlabel("Food Items")
plt.ylabel("Wastage (%)")

# to show the chart 

plt.show()


# craete a line chart using matplotlib
plt.figure(figsize=(5, 5))
plt.plot(df["food"], df["wastage"], color="blue", marker='o')
plt.xlabel("Food Items")
plt.ylabel("Wastage")
plt.grid(True)
# to show the chart 

plt.show()


# cereate a pie chart using matplotlib
plt.figure(figsize=(5, 5))
plt.pie(
    df["wastage"],
    labels=df["food"],
    autopct="%1.1f%%"
)
plt.title("Food Wastage in Canteen")
# to show the chart 

plt.show()