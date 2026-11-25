# Task 3: Even or Odd
# Write a program that accepts a number and checks whether it is even or odd.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")