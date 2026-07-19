print("Welcome to the Electricity Bill Calculator!")

unit=int(input("Enter the number of units consumed: "))
if unit<=50 and unit>0:
    a=unit*3.05
    print("Your electricity bill is: ", a)
elif unit<=100 and unit>50:
    b=unit*3.50
    print("Your electricity bill is: ", b)
elif unit<=250 and unit>100:
    c=unit*4.15
    print("Your electricity bill is: ", c)
elif unit<=1000 and unit>250:
    d=unit*5.20
    print("Your electricity bill is: ", d)
else:
    print("Invalid input. Please enter a valid number of units.")
