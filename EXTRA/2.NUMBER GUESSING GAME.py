print("Welcome to the Number Guessing Game!")

while True:
    hi=int(input("Guess a number between 1 and 100: ",))
    secret_number=26 # write a number you want to guess
    if hi==secret_number:
        print("You guessed the secret number!")
        break
    elif hi<secret_number:
        print("too low, try again.")
    else:
        print("too high, try again.")