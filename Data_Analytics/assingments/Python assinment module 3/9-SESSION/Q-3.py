# Write a function called format_price(price, currency='INR') that returns a string like '₹500' if currency is 'INR', or '$500' if currency is 'USD'.


def format_price(price, currency='INR'):
    if currency == 'INR':
        return '₹' + str(price)
    elif currency == 'USD':
        return '$' + str(price)


print(format_price(500))
print(format_price(500, 'USD'))