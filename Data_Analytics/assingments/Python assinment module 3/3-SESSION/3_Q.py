# Create a script that asks the user to input their cricket score as a string, converts it to an int, 
# and prints 'Half-century!' if the score is 50 or more, otherwise prints 'Keep going!'.
#  Use input(), int(), and if-else.

cricket_score = int(input("Enter your score : "))

if cricket_score>=50:
    print("Half-century")

else:
    print('Keep going!' )