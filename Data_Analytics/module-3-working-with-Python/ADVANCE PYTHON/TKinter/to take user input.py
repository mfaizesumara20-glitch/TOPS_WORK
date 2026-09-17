import tkinter as tk
root = tk.Tk() # create a window


root.title("My Windows App") # title of window


root.geometry("650x550") # size of window


label = tk.Label(root, text="Hello, welcome to my Windows App!" , bg="red", fg="blue", font = ('Arial', 16)) # create a label


label.pack(pady=30) # display the label



entry = tk.Entry(root,text="Enter your name", font = ('Arial', 16)) # create an entry widget
entry.pack(pady=30) # display the entry widget


button = tk.Button(root, text="Submit", font = ('Arial', 16), command=)
 


root.mainloop() # run the application # creat