# find a smalest number in anyb given list 

number = [20,52,19,18,17,48]
small = number[0]

for i in number:
    if i< small:
        small =i

print(small)