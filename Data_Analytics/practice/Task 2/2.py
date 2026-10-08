# Write a Python program to calculate electricity charges based on units consumed:
# - First 100 units: ₹5/unit
# - Next 100 units: ₹7/unit
# - Above 200 units: ₹10/unit

units = int(input("Enter the number of units consumed: "))
if units <= 100:
    charges = units * 5
elif units <= 200:
    charges = (100 * 5) + ((units - 100) * 7)
else:
    charges = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print("Electricity charges: ₹", charges)