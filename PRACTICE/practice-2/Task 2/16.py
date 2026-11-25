# Write a Python program to check voting eligibility:
# - Age 18 or above: Eligible to vote
# - Below 18: Not eligible to vote


age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")