# Task 10: Sum of Natural Numbers
# Write a program that accepts n and calculates the sum of all natural numbers from 1 to n using a loop.

n = int(input("Enter a natural number: "))

if n < 1:
    print("Please enter a natural number greater than 0.")
else:
    total = 0

    for j in range(1, n + 1):
        total += j

    print(f"The sum of natural numbers from 1 to {n} is: {total}")
