
import logic as lg

paw = lg.loginapp()

if paw:

    while True:
        print("\n***** Welcome to ATM *****")
        print("Press 1 to check Balance")
        print("Press 2 to Deposit")
        print("Press 3 to Withdraw")
        print("Press 4 to Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            lg.balanceapp()

        elif choice == 2:
            lg.depositapp()

        elif choice == 3:
            lg.withdrawapp()

        elif choice == 4:
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Access denied. Your account is locked.")
