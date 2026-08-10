# Write a Python program to check username and password:
# - Correct username and password: Login Successful
# - Wrong details: Invalid Login


correct_username = "admin"
correct_password = "123456"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid Login")