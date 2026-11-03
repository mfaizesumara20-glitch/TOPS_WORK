# Build a function called apply_coupon(price, coupon_code=None) that returns the price after a 10% discount if coupon_code is 'ZOMATO10', otherwise returns the original price.

def apply_coupon(price, coupon_code=None):
    if coupon_code == 'ZOMATO10':
        discount = price * 10 / 100
        return price - discount
    else:
        return price


print(apply_coupon(500, 'ZOMATO10'))
print(apply_coupon(500))