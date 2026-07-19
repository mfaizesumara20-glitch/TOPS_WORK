# pin= int(input("Enter your ATM PIN: "))
# withdrawal_amt= int(input("Enter the amount to withdraw: "))
# if pin== 2024:
#     print("PIN verified successfully.")
#     if withdrawal_amt>=1000:
#         print("your withdrawal is approved.")
    
#     else:
#         print("Insufficient balance.")
# else:
#     print("Invalid PIN.")




pin= int(input("Enter your ATM PIN: "))
if pin== 2024:
    print("PIN verified successfully.")
    

    balance= int(input("Enter your account balance: "))
    withdrawal_amt= int(input("Enter the amount to withdraw: "))

    if balance>=1000:
     if withdrawal_amt<=balance:
        balance= balance-withdrawal_amt
        print("your withrawal is approved.")
        print("Your remaining balance is:", balance)
     else:
        print("Insufficient balance.")
        
    else:
        print("your account balance is less than 1000. Withdrawal not allowed.")

else:
    print("Invalid PIN.")