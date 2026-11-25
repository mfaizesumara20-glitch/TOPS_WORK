# Task 11: Factorial
# Write a Python program to calculate the factorial of a number using a for loop.

num = int(input("Enter a number to calculate its factorial: "))
f = 1
for i in range(1, num + 1):
    f = f * i 
print(f"The factorial of {num} is: {f}")