# import tkinter as tk
# window = tk.Tk()

# window.title("MY First Program")
# window.geometry("500x300")
# label = tk.Label(window,text="Hello World",font=("Arial", 20))
# label.pack()

# def say_hello():
#     print('Hello')



# button = tk.Button(window,text="Click Me",command=say_hello)
# button.pack(pady=40)

# name_entry = tk.Entry(window)
# name_entry.pack()
# name = name_entry.get()

















# window.mainloop()




# import tkinter as tk
# import tkinter.messagebox as messagebox


# # This function runs when the Login button is clicked
# def login():
#     username = username_entry.get()
#     password = password_entry.get()

#     if username == "admin" and password == "1234":
#         messagebox.showinfo("Login", "Login successful")
#     else:
#         messagebox.showerror("Login", "Wrong username or password")
        


# # Create the main window
# window = tk.Tk()

# # Window title
# window.title("Login")

# # Window size
# window.geometry("400x300")

# window.configure(bg="lightblue")


# # Username label
# username_label = tk.Label(window, text="Username",font=("Arial", 30),fg="blue",bg="cyan",width=10)
# username_label.pack()

# # Username input box
# username_entry = tk.Entry(window, font=("Arial", 20))
# username_entry.pack()


# # Password label
# password_label = tk.Label(window, text="Password",font=("Arial", 30),fg="blue",bg="cyan",width=10)
# password_label.pack()

# # Password input box
# password_entry = tk.Entry(window, font=("Arial", 20), show="*")
# password_entry.pack()


# # Login button
# login_button = tk.Button(window, text="Login", font=("Arial", 20), command=login)
# login_button.pack()


# # Keep the window running
# window.mainloop()



import tkinter as tk
import tkinter.messagebox as messagebox

def login():
    usename= username_entry.get()
    password= password_entry.get()
    if usename == "admin" and password == "1234":
        messagebox.showinfo("login","Login successful")
    else:
        messagebox.showerror("login","incorrect password try again")


window = tk.Tk()
window.title("login system")
window.geometry("500x400")
window.configure(bg='lightblue')

username_lable=tk.Label(text='USERNAME',font=("Arial",20),bg='red',fg='black' )
username_lable.pack(pady=20)

username_entry=tk.Entry(font=("Arial",16))
username_entry.pack()

password_lable=tk.Label(text=("PASSWORD"),font=("Arial",20),bg="red",fg="black")
password_lable.pack(pady=20)

password_entry=tk.Entry(font=("Arial",16 ), show = "*")
password_entry.pack()

login_button=tk.Button(text="LOGIN",font=("Arial",20),command=login)
login_button.pack(pady=10)



window.mainloop()
    