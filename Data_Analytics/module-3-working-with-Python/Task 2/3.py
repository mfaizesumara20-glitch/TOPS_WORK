# Write a Python program to check a person's category based on age:
# - Below 13: Child
# - 13 to 19: Teenager
# - 20 to 59: Adult
# - 60 and above: Senior Citizen



age  = int(input("Enter the person's age: "))
if age < 13:
    print("Category: Child")
elif age <= 19:
    print("Category: Teenager")
elif age <= 59:
    print("Category: Adult")
else:
    print("Category: Senior Citizen")