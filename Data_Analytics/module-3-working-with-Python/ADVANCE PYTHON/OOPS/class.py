"""
what is class 

1. a class is nothing untill wi make it an object
2. A class is a group of its member and member fuction
3. A class is a blueprint or shadow of ant object





"""



#syntax

# class classname:
#     body of class
#     creat a function:
#          body of member function

# create an object of class


# Example

class A:
    # define an attributes of class
    name = "faize sumara"
    # create a constructor
    def __init__(self,fname,age):
        self.fname=fname # instance of class
        self.age=age


# create an object of class A
obj = A("mfaize",20) # A is an object of class A
print(obj.fname)
print(obj.age)

print ("------- mucis systterbn-------")    


