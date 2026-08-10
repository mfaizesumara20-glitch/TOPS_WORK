# Write a Python program to input three numbers and find the largest number using conditional statements.

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# if num1 >= num2 and num1 >= num3:
#     print("The largest number is:", num1)
# elif num2 >= num1 and num2 >= num3:
#     print("The largest number is:", num2)
# elif num3 >= num1 and num3 >= num2:
#     print("The largest number is:", num3)
# else:
#     print("All numbers are equal.")



num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)