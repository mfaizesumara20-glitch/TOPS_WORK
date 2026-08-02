## Conditional Statements (41–50)

# 41. Check whether a number is positive, negative, or zero.
# num = int(input("Enter a number:  "))
#
# if num>0:
#     print("the number is positive")
#
# elif num<0:
#     print("the number is negative")
# else:
#     print("the number is zero")



# 42. Find the largest of three numbers.
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
#
# if a >= b and a >= c:
#     print(a, "is the largest number")
# elif b >= a and b >= c:
#     print(b, "is the largest number")
# else:
#     print(c, "is the largest number")




# 43. Check whether a year is a leap year.
# year = int(input("Enter a year: "))
#
# if year % 400 == 0:
#     print(year, "is a Leap Year")
# elif year % 100 == 0:
#     print(year, "is not a Leap Year")
# elif year % 4 == 0:
#     print(year, "is a Leap Year")
# else:
#     print(year, "is not a Leap Year")




# 44. Check whether a person is eligible to vote.
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("You are old enough to vote")




# 45. Calculate grades based on marks.
# marks = int(input("Enter your marks: "))
#
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# elif marks >= 60:
#     print("Grade: D")
# elif marks >= 35:
#     print("Grade: E")
# else:
#     print("Fail")



# 46. Check whether a character is a vowel or consonant.
# ch = input("Enter a character: ").lower()
#
# if ch in "aeiou":
#     print("Vowel")
# else:
#     print("Consonant")



# 47. Create a simple calculator using `if-elif`.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
#
# operator = input("Enter (+, -, *, /): ")
#
# if operator == "+":
#     print("Answer =", a + b)
# elif operator == "-":
#     print("Answer =", a - b)
# elif operator == "*":
#     print("Answer =", a * b)
# elif operator == "/":
#     print("Answer =", a / b)
# else:
#     print("Invalid Operator")




# 48. Check whether a number is divisible by 7.

# num = int(input("Enter a number: "))
#
# if num % 7 == 0:
#     print("The number is divisible by 7")
# else:
#     print("The number is not divisible by 7")




# 49. Find whether a number is a multiple of 10.

# num = int(input("Enter a number: "))
#
# if num % 10 == 0:
#     print("The number is a multiple of 10")
# else:
#     print("The number is not a multiple of 10")


# 50. Check whether a student has passed (marks >= 35).

# marks = int(input("Enter your marks: "))
#
# if marks >= 35:
#     print("Pass")
# else:
#     print("Fail")