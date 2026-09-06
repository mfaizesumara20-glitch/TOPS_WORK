 # with is used to automatically close the file without using the close method

# # read a file
# with open("dictionary.txt" , "r") as file:
#     print(file.read())


# write on file

# with open("sting.txt", "w") as file:
#     print(file.write("A string is a set of characters i.e calles string"))


# with open("python modes",'r') as file:
#     content = file.read()

# print(content)



with open("python modes.txt",'w') as file:
    content = file.read()

print(content)