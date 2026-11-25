### Task 2: Simple Calculator
# Create a calculator program that accepts two numbers and performs:
# - Addition
# - Subtraction
# - Multiplication
# - Division
# - Modulus


print("-----------------------------------------")
print("Simple Calculator")
print("addition:")
print("subtraction:")
print("multiplication:")
print("division:")
print("-----------------------------------------")

choice = input("Choose an operation ( 1 to add, 2 to subtract, 3 to multiply, 4 to divide): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice == "1":
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif choice == "2":
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif choice == "3":
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please select a valid operation.")