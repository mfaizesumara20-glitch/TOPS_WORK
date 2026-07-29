file = open("dictionary.txt", "w")
txt1 = file.write('\nDictionary provides a mutable datatype')
txt2 = file.write('\nDictionary is a  datatype')

print(txt1)
print(txt2)

file.close()