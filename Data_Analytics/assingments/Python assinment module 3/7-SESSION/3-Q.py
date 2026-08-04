total = int(input("Enter your flipkart total amt: "))


if total > 2000:
    print("you are eligible for the 10% discount.")
elif total > 1000:
    print("you are eligible for the 5% discount.")
else:
    print("you are not eligible for any discount.")