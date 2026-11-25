# ### Task 8: Multiplication Table
# Create a program that accepts a number and prints its multiplication table from 1 to 10

num = int(input("Enter a number to see its multiplication table: "))

for i in  range(1,11):
    print(f"{num} x {i} = {num * i}")