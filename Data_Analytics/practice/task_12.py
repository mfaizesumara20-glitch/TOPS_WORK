# Task 12: Prime Number
# Create a program that checks whether a given number is prime or not.

def is_prime(n):
    # Prime numbers are greater than 1.
    if n <= 1:
        return False

    # Check whether any number from 2 to n - 1 divides n exactly.
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


number = int(input("Enter a number: "))

if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")