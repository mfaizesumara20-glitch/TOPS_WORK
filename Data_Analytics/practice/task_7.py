# ### Task 7: Voting Eligibility
# Write a program that accepts a person's age and checks whether the person is eligible to vote.

age = int(input("Enter your age : "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    