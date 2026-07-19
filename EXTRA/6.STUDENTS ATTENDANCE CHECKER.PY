atten= int(input("Enter the attendance percentage: "))
if atten>=90:
    print("excellent attendance")
elif atten>=89 or atten>=75:
    print("good attendance")
elif atten>=74 or atten>=50:
    print("average attendance")
else:
    print("poor attendance")