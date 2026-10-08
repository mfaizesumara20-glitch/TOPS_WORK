# w.a.p to revers a string

text  = input('enter yout string :')
rev=""
for i in text:
    rev = i+rev

print("revers string is :",rev)