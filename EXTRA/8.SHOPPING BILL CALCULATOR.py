product_price= int(input("Enter the product price: "))
quanrtity= int(input("Enter the quantity: "))
total= product_price*quanrtity
if total>=5000:
    discout=(20/100)*total
    print("#################################")
    print("total price is : ", total)
    print("discout is: ", discout)
    print("total amount is: ", total-discout)
elif total>=3000 and total<5000:
    discout=(10/100)*total
    print("#################################")
    print("total price is : ", total)
    print("discout is: ", discout)
    print("total amount is: ", total-discout)
else:
    print("there is no discount")