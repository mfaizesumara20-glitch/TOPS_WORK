# Task 13: Prime Numbers in a Range
# Write a program that accepts two numbers and displays all prime numbers between them.


start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):

    if num < 2:
        continue

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break   

    if is_prime:
        print(num)