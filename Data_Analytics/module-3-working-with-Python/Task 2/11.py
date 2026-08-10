# Write a Python program to calculate employee bonus:

# - Salary above ₹50000: 20% bonus
# - Salary between ₹30000 and ₹50000: 10% bonus
# - Below ₹30000: 5% bonus

salary = int(input("Enter the employee's salary: ₹"))

if salary > 50000:
    bonus = salary * 20 / 100
elif 30000 <= salary <= 50000:
    bonus = salary * 10 / 100
else:
    bonus = salary * 5 / 100

print(f"The employee's bonus is: ₹{bonus}")