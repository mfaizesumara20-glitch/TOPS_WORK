# calculate compound interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time in years: "))

# convert rate from percentage to decimal
rate = rate / 100

# calculate compound interest
amount = principal * (1 + rate) ** time
compound_interest = amount - principal

print("The compound interest is:", compound_interest)