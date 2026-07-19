print("------ Welcome to Mobile Recharge ------")

while True:
    print("Recharge Plans")
    print("1. ₹199 Plan")
    print("2. ₹399 Plan")
    print("3. ₹599 Plan")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("You selected the ₹199 Plan.")
        print("Amount to Pay: ₹199")

    elif choice == 2:
        print("You selected the ₹399 Plan.")
        print("Amount to Pay: ₹399")

    elif choice == 3:
        print("You selected the ₹599 Plan.")
        print("Amount to Pay: ₹599")

    elif choice == 4:
        print("Thank you for using the Mobile Recharge System!")
        break

    else:
        print("Invalid choice. Please try again.")