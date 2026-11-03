import tkinter as tk
# import database
from database import connect_database


# create a windows
root=tk.Tk()

# create a app title name

root.title("crud app windows")
root.geometry("500x500")
root.configure(bg="light blue")
# creatte a function for user input

def input_data():
    name = entry1.get()
    age = entry2.get()
    address = entry3.get()



# create lable
lable = tk.Label(root,text="Crud App Demo",bg="blue",fg="black",font=("Arial",20))
lable.pack(pady=25)


# create user lable

lable1 = tk.Label(root,text=("Name"),font=("arial",10))
entry1 = tk.Entry(root,text=("Enter your name  :"))
lable1.pack(pady=10)
entry1.pack(pady=10)


lable2 = tk.Label(root,text=("Age"),font=("arial",10))
entry2 = tk.Entry(root,text=("Enter your age  :"))
lable2.pack(pady=10)
entry2.pack(pady=10)



lable3 = tk.Label(root,text=("Address"),font=("arial",10))
entry3 = tk.Entry(root,text=("Enter your Address  :"))
lable3.pack(pady=10)
entry3.pack(pady=10)


# for button

button = tk.Button(root,text=("submit  :"),command=input_data)
button.pack(pady=10)



# create windows loop or dis[play the windows app]

tk.mainloop()