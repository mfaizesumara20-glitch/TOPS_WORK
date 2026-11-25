# Write a Python program to calculate ticket price:
# - Age below 12: ₹100
# - Age 12 to 60: ₹200
# - Age above 60: ₹150

age = int(input("Enter the age of the person: "))

if age < 12:
    print("The ticket price is: ₹100")
elif 12 <= age <= 60:
    print("The ticket price is: ₹200")
else:
    print("The ticket price is: ₹150")

