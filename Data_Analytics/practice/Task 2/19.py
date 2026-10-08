# Write a Python program to suggest a mobile plan:
# - Data usage below 2GB: Basic Plan
# - 2GB to 5GB: Standard Plan
# - Above 5GB: Premium Plan

data_usage = float(input("Enter your monthly data usage in GB: "))
if data_usage < 2:
    print("You should choose the Basic Plan.")
elif 2 <= data_usage <= 5:
    print("You should choose the Standard Plan.")
else:   
    print("You should choose the Premium Plan.")