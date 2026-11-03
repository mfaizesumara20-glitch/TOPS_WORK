import pandas as pd
import matplotlib.pyplot as plt

data = {
    "food_name": ["Pizza", "Burger", "Pasta", "Salad","pav bhaji", "Dosa", "Idli", "Samosa", "Biryani", "Tacos"],
    "wastage": [20,10,40,15,45,12,15,30,10,6]



}


df = pd.DataFrame(data)
print(df)


highest_waste = df["wastage"].max()
print('highest food wastage',highest_waste,"kg" )


low_waste = df["wastage"].min()
print('lowest food wastage',low_waste,"kg" )


plt.title("Food Wastage Distribution")
# plt.pie([highest_waste,low_waste], labels=['Highest', 'Lowest'], autopct='%1.1f%%',colors=['red','green'])

plt.pie(df["wastage"], labels=df["food_name"], autopct='%1.1f%%',colors=['#ff9999','#66b3ff',"#99ff99",'#ffcc99','#c2c2f0','#ffb3e6','#c2f0c2','#ff6666','#c2d6d6','#ffb366'])

plt.show()






# import pandas as pd
# import matplotlib.pyplot as plt

# data = {
#     "food_name": ["Pizza", "Burger", "Pasta", "Salad","pav bhaji", "Dosa", "Idli", "Samosa", "Biryani", "Tacos"],
#     "wastage": [20,10,40,15,45,12,15,30,10,6]



# }


# df = pd.DataFrame(data)
# print(df)


# highest_waste = df["wastage"].max()
# print('highest food wastage',highest_waste,"kg" )


# low_waste = df["wastage"].min()
# print('lowest food wastage',low_waste,"kg" )

# plt.title("Food Wastage Distribution")
# plt.pie([total_food], labels=['Food Items'], autopct='%1.1f%%',)



# plt.show()