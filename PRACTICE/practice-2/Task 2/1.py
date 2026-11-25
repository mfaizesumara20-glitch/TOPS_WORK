# Write a Python program to input student marks and display the grade:
# - 90 and above: Grade A
# - 75 to 89: Grade B
# - 50 to 74: Grade C
# - 35 to 49: Grade D
# - Below 35: Fail


mark = int(input("Enter the student's marks: "))

if mark >= 90:
    print("Grade: A")
elif mark >= 75:
    print("Grade: B")
elif mark >= 50:
    print("Grade: C")
elif mark >= 35:
    print("Grade: D")
else:
    print("Fail")