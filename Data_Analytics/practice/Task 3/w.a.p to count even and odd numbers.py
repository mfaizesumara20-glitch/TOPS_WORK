# w.a.p to count even and odd numbers 
number = [10, 85, 66, 48, 95, 12, 36]

even = 0
odd = 0

for i in number:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print('total even', even)
print('total odd', odd)