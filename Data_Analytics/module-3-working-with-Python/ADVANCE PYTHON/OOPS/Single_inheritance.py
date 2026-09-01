"""
What is single inheritance?

A one parant class access by its only one child class i.e songle inheritance

or

A => B


"""

"""
syntax

class A:
    create member function


    def __init__(self):
        body of member function

       def info():
       body of member function

class B(A):
    member function():


obj = B()

call the method

"""


# class A:
#     def __init__(self,name):
#         self.name=name

#     def info(self):
#         print("The name of users is :",self.name)

# class B(A):
#     def add(self,address):
#         self.address=address
#         print("The address of users is :",self.address)

# obj = B("faize")
# obj.info()
# obj.add("150 feet ring road")





class A:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("The name of user is:", self.name)


class B(A):
    def add(self, address):
        self.address = address
        print("The address of user is:", self.address)


obj = B("faize")
obj.info()
obj.add("150 feet ring road")