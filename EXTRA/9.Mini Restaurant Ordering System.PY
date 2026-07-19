# print("--------welcome to the mini restaurant--------")
# print("Menu:")
# print("1. Pizza - ₹250")
# print("2. Burger - ₹150")
# print("3. Sandwich - ₹120")

# while True:
#     order = int(input("enter the number of the corosponding item you want to order : "))
#     price1 = 250
#     price2 = 150
#     price3 = 120
#     if order == 1:
#         print("You have ordered Pizza.")
#         print("Price: ", price1)
        
#     elif order == 2:
#         print("You have ordered Burger.")
#         print("Price: ", price1 + price2)
        
#     elif order == 3:
#         print("You have ordered Sandwich.")
#         print("Price: ", price1 + price2 + price3)

#     else:
#         print("Invalid order. Please select a valid item.")





print("-------- Welcome to the Mini Restaurant --------")

while True:
    print("Menu:")
    print("1. Pizza - ₹250")
    print("2. Burger -4")
    print("3. Sandwich - ₹120")
    print("4. Exit")

    order = int(input("Enter your choice: "))

    if order == 1:
        qty = int(input("Enter quantity: "))
        total = qty * 250
        print("You ordered", qty, "Pizza(s).")
        print("Total Price: ₹", total)

    elif order == 2:
        qty = int(input("Enter quantity: "))
        total = qty * 150
        print("You ordered", qty, "Burger(s).")
        print("Total Price: ₹", total)

    elif order == 3:
        qty = int(input("Enter quantity: "))
        total = qty * 120
        print("You ordered", qty, "Sandwich(es).")
        print("Total Price: ₹", total)

    elif order == 4:
        print("Thank you for visiting our restaurant!")
        break

    else:
        print("Invalid choice. Please try again.")