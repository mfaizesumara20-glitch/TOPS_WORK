# Write a Python program to check driving license eligibility:
# - Age 18 or above: Eligible
# - Below 18: Not Eligible


age = int(input("Enter your age: "))
if  age >= 18:
    print("You are eligible for a driving license.")
else:
    print("You are not eligible for a driving license.")