"""
what is object 

1. a object is an instance of class
2. An object is an example of class





"""


class Car:
    name = "Alto 800"
    def __init__(self,carname,price,year):
        self.carname = carname
        self.price = price
        self.year = year


obj=Car("BMW" ,100000,2024) # Car() is an object of class Car
print("car name :",obj.carname)
print("car price :",obj.price)
print("car year :",obj.year)

