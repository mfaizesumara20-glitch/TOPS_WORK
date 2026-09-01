"""
encapsulation is used to wrap up a data in a single object
data access in encapsulation by access modifier or private | public | protective


encapsulation is used for visibility of data via 

private | public | protective
"""

# public: accesseble anywhere

class employee:
    def __init__(self,name):
        self.name=name # access via public
        # create a public metode
    def display_employee(self):
        print(self.name)

obj= employee("faize")
obj.display_employee
print(obj.name)



# private