## Lists (21–30)

# 21. Create a list of five numbers and print it.
num = [ 5,5,4,9,8,3,10,15,20]
print(num)

# 22. Add an element to a list.
c = num.append(6)
print(num)


# 23. Remove an element from a list.
f = num.pop(4)
print(num)


# 24. Find the largest element in a list.
r = max(num)
print(r)


# 25. Find the smallest element in a list..
t = min(num)
print(t)

# 26. Calculate the sum of all elements in a list.
l = sum(num)
print(l)

# 27. Count how many times an element appears in a list.
hi = int(input("Enter the number: "))
res = (num.count(hi))
print(hi,"is",res,"times in the list")



# 28. Reverse a list.
q = num.reverse()
print(num)


# 29. Sort a list in ascending order.
k = num.sort()
print(num)


# 30. Remove duplicate elements from a list.
o = set(num)
print(o)

