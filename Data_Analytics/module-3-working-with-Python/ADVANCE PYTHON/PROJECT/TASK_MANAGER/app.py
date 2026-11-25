# create a database connection 

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl as xl 
import numpy as np

# connect database

conn = sqlite3.connect("task_manager_app_db")

# create a crud app of task manager app

# insert data using sqlite3 in task_manager_app_db and insert or add multiple employee in employee table

cur = conn.cursor()
insert = [

     (1, "John Doe", 9998003827, 50000, "2023-01-01", "hi"),
     (2, "Jane Smith", 9998003828, 60000, "2023-01-02", "hello"),
     (3, "Bob Johnson", 9998003829, 70000, "2023-01-03", "good"),
     (4, "Alice Williams", 9998003830, 80000, "2023-01-04", "great"),
     (5, "Charlie Brown", 9998003831, 90000, "2023-01-05", "excellent"),
     (6, "David Lee", 9998003832, 100000, "2023-01-06", "fantastic"),
 ]

 # query execute 
cur.executemany(

     """
 insert or replace into feedback(fid,name, mobile, salary, created_date, comment) values(?,?,?,?,?,?)
     
    
     """, insert
 )


conn.commit()
print("Data inserted successfully in feedback table")


# display all employee data from feedback table 

query = "select * from feedback"

df = pd.read_sql(query , conn)

print("data fetched successfully from feedback table\n", df)


# dels = "trancate table feedback"


# finding the max salary

max_salary = df["salary"].max()

print("----------------------------------------")
print(f"Maximum salary: {max_salary}")
print("----------------------------------------")


# finding the min salary
min_salary = df["salary"].min()

print("----------------------------------------")
print(f"Minimum salary: {min_salary}")
print("----------------------------------------")

## finding the average salary
avg_salary = df["salary"].mean()

print("----------------------------------------")
print(f"Average salary: {avg_salary}")
print("----------------------------------------")

# highest salary employee name 

highest_salary_employee = df.loc[df["salary"].idxmax(),["name","salary"]]
print("----------------------------------------")
print(f"Highest salary employee:\n {highest_salary_employee}")
print("----------------------------------------")




conn.close()


