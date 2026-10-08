# w.a.p to find sum of list of elements

# num = [12,58,55,10,25,95,]
# total=0
# for x in num:
#     total = total+x

# print(total)



numbers = [10, 25, 7, 42, 18]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)