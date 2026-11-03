# how to connect with database using python
import sqlite3 

# create a database 

conn = sqlite3.connect("task_manager_app_db")
print("Database created successfully")

conn.close()