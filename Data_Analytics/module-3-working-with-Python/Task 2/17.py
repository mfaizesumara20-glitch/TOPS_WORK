# Write a Python program to check password strength:
# - Length less than 6: Weak
# - Length 6 to 10: Medium
# - Length above 10: Strong

password = input("Enter your password: ")
if len(password) < 6:
    print("Your password is Weak.") 
elif 6 <= len(password) <= 10:
    print("Your password is Medium.")
else:
    print("Your password is Strong.")
    