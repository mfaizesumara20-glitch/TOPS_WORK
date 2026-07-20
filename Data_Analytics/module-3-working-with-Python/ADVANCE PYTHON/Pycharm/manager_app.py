# create a manager app
# print('hello world')
# w.a.p to find a compund interest
import math

# Program to calculate Compound Interest using math library

p = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate (%): "))
t = float(input("Enter the time (in years): "))

# Calculate the final amount
amount = p * math.pow((1 + r / 100), t)

# Calculate compound interest
compound_interest = amount - p

print("Final Amount =", amount)
print("Compound Interest =", compound_interest)