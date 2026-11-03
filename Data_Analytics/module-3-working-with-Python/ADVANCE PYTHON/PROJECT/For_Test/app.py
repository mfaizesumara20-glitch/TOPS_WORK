import sqlite3 
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl as xl
import numpy as np

conn = sqlite3.connect("The_Test.db")
print ("database created")

cur = conn.cursor()

cur.executescript(
    """
create table if not exist departnment(depid integer primary key AUTOINCREMENT,
department_name text,
location text
)

create table if not exist (depid integer primary key AUTOINCREMENT

)




"""




)