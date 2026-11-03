# import tkinter as tk
# import ttkbootstrap as ttkb




# # def compound_interest(principal, rate, time):
# #     amount = principal * (1 + rate / 100) ** time
# #     ci = amount - principal

# #     return ci


# # principal = float(input("Enter principal amount: "))
# # rate = float(input("Enter rate of interest: "))
# # time = float(input("Enter time in years: "))

# # result = compound_interest(principal, rate, time)



# # print("Compound Interest =", result)




# root=tk.Tk()
# root.title("COMPOUND INTEREST")
# root.geometry("500x500")
# root.config(bg="light blue")

# lable1=tk.Label(text="principal amt",font=("Arial",15),fg="black")
# lable1.pack(pady=10)

# entry1=tk.Entry(bg="gray")
# entry1.pack(pady=10)




# lable2=tk.Label(text="rate",fg="black")
# lable2.pack()

# entry2=tk.Entry(bg="gray")
# entry2.pack()




# lable3=tk.Label(text="years",fg="black")
# lable3.pack()

# entry3=tk.Entry(bg="gray")
# entry3.pack()


# root.mainloop()






import tkinter as tk
import mysql.connector


# Compound Interest Function
def compound_interest(princple, rate, years):
    amount = princple * (1 + rate / 100) ** years
    ci = amount - princple

    return ci


# Calculate Button Function
def calculate():

    princple = float(entry1.get())
    rate = float(entry2.get())
    years = float(entry3.get())

    interest = compound_interest(princple, rate, years)

    result_label.config(
        text=f"Compound Interest = ₹{interest:.2f}"
    )

    # Connect to MySQL
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="compound_interest"
    )

    cursor = db.cursor()

    # Save data
    query = """
    INSERT INTO calculation
    (princple, rate, years, interest)
    VALUES (%s, %s, %s, %s)
    """

    values = (princple, rate, years, interest)

    cursor.execute(query, values)

    db.commit()

    cursor.close()
    db.close()


# Tkinter Window
root = tk.Tk()

root.title("COMPOUND INTEREST")
root.geometry("500x500")
root.config(bg="light blue")


lable1 = tk.Label(
    root,
    text="Principal Amount",
    font=("Arial", 15),
    fg="black",
    bg="light blue"
)
lable1.pack(pady=10)


entry1 = tk.Entry(
    root,
    bg="white",
    font=("Arial", 13),
    width=25
)
entry1.pack(pady=10)


lable2 = tk.Label(
    root,
    text="Rate (%)",
    font=("Arial", 15),
    fg="black",
    bg="light blue"
)
lable2.pack(pady=5)


entry2 = tk.Entry(
    root,
    bg="white",
    font=("Arial", 13),
    width=25
)
entry2.pack(pady=10)


lable3 = tk.Label(
    root,
    text="Years",
    font=("Arial", 15),
    fg="black",
    bg="light blue"
)
lable3.pack(pady=5)


entry3 = tk.Entry(
    root,
    bg="white",
    font=("Arial", 13),
    width=25
)
entry3.pack(pady=10)


button = tk.Button(
    root,
    text="CALCULATE",
    font=("Arial", 13, "bold"),
    bg="green",
    fg="white",
    width=15,
    command=calculate
)
button.pack(pady=20)


result_label = tk.Label(
    root,
    text="Compound Interest = ₹0.00",
    font=("Arial", 16, "bold"),
    fg="black",
    bg="light blue"
)
result_label.pack(pady=10)


root.mainloop()