"""
A constructor is an same name of class
or
A constructor is ame name of class whenever we create an object of class constructor autometically 

note : A constructor is a default method that can be defined as __init__(self) argument
 

"""


class collage:
    collagename = "HNS collage"
    def __init__(self,name,address,trustname):
        self.name=name
        self.address=address
        self.trustname=trustname

obj = collage("atmya collage","150 feet ring road","gurukul")

print(obj.name)
print(obj.address)
print(obj.trustname)