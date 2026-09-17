import tkinter as tk
root = tk.Tk() # create a window
root.title("My Windows App") # title of window
root.geometry("650x550") # size of window
label = tk.Label(root, text="Hello, welcome to my Windows App!" , bg="red", fg="blue", font = ('Arial', 16)) # create a label
label.pack(pady=30) # display the label

root.mainloop() # run the application