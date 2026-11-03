# create task manager app using sqllite database 

1. install all depandencies
2. pip install pandas numpy openpyxl matplotlib
3. create some python file for perform **crud** operation


# what is crud operation 

**c** : create
**r** : read
**u** : update
**d** : delete


# create a database connection and tables via sqllite

**create a database**

'''
# how to connect with database using python
import sqlite3 

# create a database 

conn = sqlite3.connect("task_manager_app_db")
print("Database created successfully")

conn.close()

'''

**create a table**

'''
# create a table via sqlite3 in task_manager_app_db

import sqlite3

# create a database connection
conn = sqlite3.connect("task_manager_app_db")

# create a table in databse

cur = conn.cursor()
cur.execute(


  """ 
  create table if not exists tasks(
  id integer primary key autoincrement,
  title text,
  assign text,
  status text,
  comment text
  )
  """
)

# print message
print("Table created successfully in database")

# save query
conn.commit()
conn.close()
'''