# what is module in python


- a module is an small peace of file that can be save in python  using .py i.e called module

- a module is saved with .py i.e called module in python

- there are three types of module

  
  1. user define module
  2. pre define module 
  3. third party module


# user define module 

 - user defined module is defined by user save with .py file 
 - examples 
 - name.py
 ```
 name=input("Enter your Name : ")
 print("Your name is :",name)
 ``` 




# pre define module

 - pre define module is a system define module 

 - pre define module is used to calculate some powers | math functions 

 example

 ***
import  math
 print(math.pow(5, 2))
 print(math.sqrt(25))
 print(math.floor(10.8762486))
 print(math.ceil(10.8762486))
 
 import calendar
 print(calendar.month(2024, 6))
 print(calendar.calendar(2020))

 import random
 #otp generate 4 digit
 print(random.randint(1111, 9999))

 ***


# third party module or librarise

 - third party module is used to in package format

 - third party module is always installable 

 - third party module installs with **pip**

 - pip stands for **python install package**


# note :  create a  programe dataframe and show emplyee detaile in dataframe with tabuler layout 

 **examples**

 ***
 import pandas as pd
 employee={

    "fname":["John","Smith","Peter","David"],
    "lname":["Doe","Johnson","Williams","Brown"]
 }

 print(pd.DataFrame(employee))
 ***