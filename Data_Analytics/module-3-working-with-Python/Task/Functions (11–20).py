# 11. Create a function to add two numbers.
# def add(a,b):
#     c = a+b
#     return c
# print(add(5,5))



# 12. Create a function to calculate the factorial of a number.

# num = int(input('Enter a number you want the factorial for :' ))
#
# f = 1
# for i in range(1,num+1):
#     f *= i
#
# print(f)





# 13. Write a function to check whether a number is prime.
# def is_prime(number):
#     if number <= 1:
#         return False
#
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#
#     return True
#
#
# num = int(input("Enter a number: "))
#
# if is_prime(num):
#     print(num, "is a Prime Number")
# else:
#     print(num, "is not a Prime Number")



# 14. Create a function to find the largest of three numbers.
# def largest_Number(a,b,c):
#     if a>b and a>c :
#         print('a is the largest number')
#     elif b>a and b>c :
#         print('b is the largest number')
#     elif c>a and c>b :
#         print('c is the largest number')
#     else:
#         print('invalid number')
#
# print =largest_Number(10,20,30)



# 15. Write a function to count vowels in a string.

# def count_vowels(text):
#     count = 0
#
#     for ch in text.lower():
#         if ch in "aeiou":
#             count += 1
#
#     return count
# word = input("Enter a string: ")
# print("Number of vowels:", count_vowels(word))


# 16. Create a function to reverse a string.
# def reverse_string(text):
#     return text[::-1]
#
#
# word = input("Enter a string: ")
# print("Reversed string:", reverse_string(word))


# 17. Write a function to calculate the square of a number.
#
# def square(num):
#     return num * num
#
#
# number = int(input("Enter a number: "))
# print("Square:", square(number))


# 18. Create a function to return the sum of elements in a list.

# def sum_list(numbers):
#     total = 0
#
#     for i in numbers:
#         total += i
#
#     return total
#
#
# numbers = [10, 20, 30, 40, 50]
#
# print("Sum:", sum_list(numbers))


# 19. Write a function to find the maximum number in a list.

# def find_max(numbers):
#     maximum = numbers[0]
#
#     for i in numbers:
#         if i > maximum:
#             maximum = i
#
#     return maximum
#
#
# numbers = [10, 45, 23, 89, 67]
#
# print("Maximum number:", find_max(numbers))

# 20. Create a function that accepts a name and prints a greeting message.

# def greet(name):
#     print("Hello,", name + "! Welcome.")
#
#
# user_name = input("Enter your name: ")
# greet(user_name)