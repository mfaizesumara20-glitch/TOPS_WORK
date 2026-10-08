# ### Task 6: Student Result
# Create a program that accepts marks of five subjects and calculates:
# - Total marks
# - Percentage
# - Grade

marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total = sum(marks)
percentage = (total / 500) * 100

if percentage >= 80:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "D"

print(f"Total marks: {total}")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")