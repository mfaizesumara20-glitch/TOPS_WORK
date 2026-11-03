import mysql.connector
from mysql.connector import errors

def connect_database():
    try:
        
        db = mysql.connector.connect(
            host="localhost",
            user="root",              # Aapka MySQL username (default: root)
            password="", # Aapka MySQL password
            database="mySQL_app"  # Aapke database ka naam
        )
        print("Database connection successful!")
    except Exception as e:
        print(f"Error connecting to database : {e}")