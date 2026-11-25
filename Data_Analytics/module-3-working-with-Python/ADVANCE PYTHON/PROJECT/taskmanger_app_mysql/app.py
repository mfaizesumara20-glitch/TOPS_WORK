import matplotlib.pyplot as pyt
import openpyxl
import mysql.connector
from mysql.connector import Error
import pandas as pd
import numpy as np 

# create a database conn

try:

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "admin",
        database = "task_manager_db_app"
    )

    if conn.is_connected():
        print("connection stablished successfully")
        cursor = conn.cursor()

except Error as e:
    print(f"something went wrong please check {e}")