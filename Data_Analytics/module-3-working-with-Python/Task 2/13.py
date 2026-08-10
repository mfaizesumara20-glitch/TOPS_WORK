# Write a Python program to check withdrawal:
# - Balance sufficient: Allow withdrawal
# - Insufficient balance: Show error message

balance = int(input("Enter the current balance: ₹"))
withdrawal_amount = int(input("Enter the amount to withdraw: ₹"))

if withdrawal_amount <= balance:
    print("Withdrawal successful.")
else:
    print("Error: Insufficient balance.")