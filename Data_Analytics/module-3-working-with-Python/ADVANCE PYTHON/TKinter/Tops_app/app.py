# import tkinter as tk
# import ttkbootstrap as ttkb
# import messagebox 

# root = tk.Tk()

# root.title("LOGIN APP")
# root.geometry("600x600")
# root.config(bg="light blue")



# lable1=tk.Label(text="USERNAME",bg="light gray",font=("Arial",15))
# lable1.pack(pady=50)


# entry1=tk.Entry(bg="light gray",font=("Arial",15))
# entry1.pack()





# lable2=tk.Label(text="PASSWORD",bg="light gray",font=("Arial",15))
# lable2.pack(pady=50)


# entry2=tk.Entry(bg="light gray",font=("Arial", 15))
# entry2.pack()


# root.mainloop()





import tkinter as tk
import ttkbootstrap as ttkb
from tkinter import messagebox


# ---------------- LOGIN FUNCTION ----------------
def login():
    mobile = mobile_entry.get()
    password = password_entry.get()

    if mobile == "" or password == "":
        messagebox.showwarning(
            "Warning",
            "Please enter mobile number and password"
        )

    elif mobile == "1234567890" and password == "1234":
        messagebox.showinfo(
            "Login",
            "Login successful!"
        )

        welcome_label.config(
            text="Welcome Back!",
            bootstyle="success"
        )

    else:
        messagebox.showerror(
            "Login Failed",
            "Invalid mobile number or password"
        )


# ---------------- SHOW / HIDE PASSWORD ----------------
def show_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_button.config(text="Hide")
    else:
        password_entry.config(show="*")
        show_button.config(text="Show")


# ---------------- FORGOT PASSWORD ----------------
def forgot_password():
    messagebox.showinfo(
        "Forgot Password",
        "Password reset option will be available soon."
    )


# ---------------- ANIMATION ----------------
def animate():
    x = welcome_label.winfo_x()

    if x < 180:
        welcome_label.place(x=x + 2, y=40)
        root.after(10, animate)


# ---------------- MAIN WINDOW ----------------
root = ttkb.Window(themename="flatly")

root.title("TOPS Career Center")
root.geometry("600x600")
root.resizable(False, False)


# ---------------- MAIN TITLE ----------------
title_label = ttkb.Label(
    root,
    text="TOPS Career Center",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=(80, 10))


# ---------------- WELCOME MESSAGE ----------------
welcome_label = ttkb.Label(
    root,
    text="Welcome Back!",
    font=("Arial", 18, "bold")
)

welcome_label.place(x=0, y=40)


# ---------------- SUBTITLE ----------------
subtitle_label = ttkb.Label(
    root,
    text="Sign in to continue to TOPS Career Center",
    font=("Arial", 11)
)

subtitle_label.pack(pady=5)


# ---------------- LOGIN FRAME ----------------
login_frame = ttkb.Frame(
    root,
    padding=30
)

login_frame.pack(pady=30)


# ---------------- MOBILE NUMBER ----------------
mobile_label = ttkb.Label(
    login_frame,
    text="Mobile Number",
    font=("Arial", 12, "bold")
)

mobile_label.pack(anchor="w", pady=(5, 5))


mobile_entry = ttkb.Entry(
    login_frame,
    width=35,
    font=("Arial", 13)
)

mobile_entry.pack(pady=(0, 15))


# ---------------- PASSWORD ----------------
password_label = ttkb.Label(
    login_frame,
    text="Password",
    font=("Arial", 12, "bold")
)

password_label.pack(anchor="w", pady=(5, 5))


password_entry = ttkb.Entry(
    login_frame,
    width=35,
    font=("Arial", 13),
    show="*"
)

password_entry.pack(pady=(0, 5))


# ---------------- SHOW PASSWORD ----------------
show_button = ttkb.Button(
    login_frame,
    text="Show",
    bootstyle="secondary",
    command=show_password
)

show_button.pack(pady=5)


# ---------------- FORGOT PASSWORD ----------------
forgot_button = ttkb.Button(
    login_frame,
    text="Forgot password?",
    bootstyle="link",
    command=forgot_password
)

forgot_button.pack(pady=5)


# ---------------- SIGN IN BUTTON ----------------
login_button = ttkb.Button(
    login_frame,
    text="SIGN IN",
    bootstyle="primary",
    width=25,
    command=login
)

login_button.pack(pady=20)


# ---------------- FOOTER ----------------
footer_label = ttkb.Label(
    root,
    text="© TOPS Technologies | Career Center",
    font=("Arial", 9)
)

footer_label.pack(side="bottom", pady=20)


# ---------------- START ANIMATION ----------------
root.after(100, animate)


# ---------------- RUN APP ----------------
root.mainloop()

