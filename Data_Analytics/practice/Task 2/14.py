# Write a Python program to apply discount:
# - Purchase above ₹10000: 20% discount
# - Purchase above ₹5000: 10% discount
# - Otherwise: No discount


purchase_amount = int(input("Enter the purchase amount: ₹"))

if purchase_amount > 10000:
    discount = purchase_amount * 20 / 100
elif purchase_amount > 5000:
    discount = purchase_amount * 10 / 100
else:
    discount = 0    

print(f"The discount is: ₹{discount}")