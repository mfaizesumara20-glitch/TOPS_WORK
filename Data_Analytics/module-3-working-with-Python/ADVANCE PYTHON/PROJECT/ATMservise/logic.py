# balance = 15000
# pin = 1234


# def loginapp():
#     attempts = 0

#     while attempts < 3:
#         res = int(input("Enter your pin:"))

#         if res == pin:
#             print("Welcome user")
#             return True
#         else:
#             print("Invalid pin")
#             attempts += 1

#     print("You have used all 3 attempts.")
#     return False   
 
# print(loginapp())



# def balanceapp():
#     print("Your balance is :", balance)






# def depositapp():
#     dep = int(input("Enter your deposit amount :"))
#     c = balance + dep
#     if dep == 0:
#         print("Invalid deposit amount can not deposit")
#     elif dep > 50000:
#         print("Deposit limit exeeded")
#     else:
#         print("your balance is ",c)

# print(depositapp())

# def withdrawapp():
#     wd = int(input("Enter your withdrawal amount: "))

#     if wd == 0:
#         print("Invalid amount, cannot withdraw.")
#     elif wd > 15000:
#         print("Insufficient balance to withdraw.")
#     else:
#         c = balance - wd
#         print("Your remaining balance is:", c)

# print(withdrawapp())



balance = 15000
pin = 1234


def loginapp():
    attempts = 0

    while attempts < 3:
        res = int(input("Enter your pin: "))

        if res == pin:
            print("Welcome user!")
            return True
        else:
            print("Invalid pin")
            attempts += 1

    print("You have used all 3 attempts.")
    return False


def balanceapp():
    print("Your balance is:", balance)


def depositapp():
    global balance

    dep = int(input("Enter your deposit amount: "))

    if dep <= 0:
        print("Invalid deposit amount.")
    elif dep > 50000:
        print("Deposit limit exceeded.")
    else:
        balance += dep
        print("Your updated balance is:", balance)


def withdrawapp():
    global balance

    wd = int(input("Enter your withdrawal amount: "))

    if wd <= 0:
        print("Invalid amount, cannot withdraw.")
    elif wd > balance:
        print("Insufficient balance.")
    elif wd > 15000:
        print("Withdrawal limit exceeded.")
    else:
        balance -= wd
        print("Your remaining balance is:", balance)
