password = input("Enter your password: ")

has_digit = False

for letter in password:
    if letter.isdigit():
        has_digit = True

if len(password) >= 8:
    if has_digit:
        print("Strong Password")
    else:
        print("Weak Password")
else:
    print("Weak Password")