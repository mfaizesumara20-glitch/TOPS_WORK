# Write a function total_cart_amount(prices) that takes a list of product prices as strings (like ['199.99', '49', '350.75']) and returns the total as a float.
# Print the result for a sample Flipkart-style cart. Use float() to convert each string before summing.


# price = ['122','199.32','70']

# #total_cart = (float(price))
# price = [float(item) for item in price]
# print(price)
# print(type(item))

def total_cart_amount(prices):
    total = 0

    for price in prices:
        total += float(price)

    return total


# Sample Flipkart-style cart
cart_prices = ['199.99', '49', '350.75']

total = total_cart_amount(cart_prices)

print(total)