# Write a Python script that uses indentation correctly to check if a Flipkart product's price is above 1000; if yes, print 'Eligible for free delivery', else print 'Delivery charges apply'. 
# Use an if-else block and make sure your indentation is consistent.

product_price=int(input("Enter the price of the product : "))

if product_price>1000:
    print("Eligible for free delivery")

else:
    print("Delivery charges apply")
    