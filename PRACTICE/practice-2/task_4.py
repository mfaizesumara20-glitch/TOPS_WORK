# Task 4: Positive, Negative or Zero
# Create a program that accepts a number and determines whether it is positive, negative, or zero.

num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is zero.")