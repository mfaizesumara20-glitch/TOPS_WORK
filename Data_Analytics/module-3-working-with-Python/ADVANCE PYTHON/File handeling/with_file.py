 # with is used to automatically close the file without using the close method

# # read a file
# with open("dictionary.txt" , "r") as file:
#     print(file.read())


# write on file

with open("sting.txt", "w") as file:
    print(file.write("A string is a set of characters i.e calles string"))


