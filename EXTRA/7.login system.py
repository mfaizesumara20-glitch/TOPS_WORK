# a=input("Enter your username: ")
# b=input("Enter your password: ")
# while True:
#     if a=="admin" and b=="1234":
#         print("Login successful")
        
#     elif a=="user" and b=="5678":
#         print("Login successful")
        
#     elif a=="user" and b=="5678":
#         print("Login successful")
        
#     else:
#         print("OUT OF ATTEMPTS ACCOUNT LOCKED!!!.")
#         break



attempts = 3

while attempts > 0:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "admin" and password == "1234":
        print("Login successful")
        break
    else:
        attempts -= 1
        print("Incorrect username or password.")
        print("Attempts left:", attempts)

if attempts == 0:
    print("OUT OF ATTEMPTS! ACCOUNT LOCKED!")