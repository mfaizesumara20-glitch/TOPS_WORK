# Write a Python program to display weather conditions:
# - Below 10°C: Cold
# - 10°C to 30°C: Normal
# - Above 30°C: Hot


temperature = float(input("Enter the temperature in Celsius: "))
if temperature < 10:    
    print("The weather is Cold.")
elif 10 <= temperature <= 30:
    print("The weather is Normal.")
else:
    print("The weather is Hot.")