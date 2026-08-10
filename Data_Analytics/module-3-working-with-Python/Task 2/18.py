# Write a Python program to calculate BMI category:
# - BMI below 18.5: Underweight
# - 18.5 to 24.9: Normal
# - 25 to 29.9: Overweight
# - 30 and above: Obese

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("You are Underweight.")
elif 18.5 <= bmi <= 24.9:
    print("You are Normal.")
elif 25 <= bmi <= 29.9:
    print("You are Overweight.")
else:
    print("You are Obese.")