# Write a script that uses the os module to create a new folder named 'MyDownloads' in your current working directory, then print the absolute path of the new folder.




import os

folder = "MyDownloads"

os.mkdir(folder)

print("Folder created!")
print("Absolute path:", os.path.abspath(folder))


