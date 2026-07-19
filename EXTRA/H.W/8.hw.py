# w.a.p to find choice based calculator choice a number
 
print("------calculator------")
print("1 for add")
print("2 for sub")
print("3 for multi")
print("4 for div")
print("5 for exit")

while True:
    num=(input("Enter a number : "))
    if num=='1':
        print("you have chosen addition")
        a=int(input("ENTER A NUMBER : "))
        b=int(input("ENTER A NUMBER : "))
        c=a+b
        print(c)
    
    if num=='2':
        print("you have chosen subtraction")
        a=int(input("ENTER A NUMBER : "))
        b=int(input("ENTER A NUMBER : "))
        c=a-b
        print(c)

    if num=='3':
        print("you have chosen multiply")
        a=int(input("ENTER A NUMBER : "))
        b=int(input("ENTER A NUMBER : "))
        c=a*b
        print(c)

    if num=='4':
        print("you have chosen division")
        a=int(input("ENTER A NUMBER : "))
        b=int(input("ENTER A NUMBER : "))
        c=a/b
        print(c)

    if num=='5':
        print("THE PROGRAM HAS ENDED THANK YOU")
        
        break

    