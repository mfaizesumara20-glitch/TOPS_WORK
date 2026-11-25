import matplotlib.pyplot as plt
import pandas as pd
data = {
    "bottles":["red", "green", "blue", "yellow","purple","orange","pink"],
    "values":[10, 15, 15, 12, 20, 11, 30]
}

df = pd.DataFrame(data)
print(df)

## bar graph

# plt.figure(figsize=(5,5))
# plt.bar(df["bottles"],df["values"],color="green")
# plt.title("TOTAL BOTTLES")
# plt.xlabel("bottles")
# plt.ylabel("values")


# plt.show()


## line graph

plt.figure(figsize=(5,5))
plt.plot(df["bottles"],df["values"],color=('blue'),marker='o')
plt.xlabel("bottles")
plt.ylabel("values")
plt.grid(True)
plt.show()