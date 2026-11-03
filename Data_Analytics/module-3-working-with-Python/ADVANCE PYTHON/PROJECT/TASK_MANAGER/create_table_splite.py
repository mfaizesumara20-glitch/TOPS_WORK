# create a table via sqlite3 in task_manager_app_db

import sqlite3

# create a database connection
conn = sqlite3.connect("task_manager_app_db")

# create a table in databse

cur = conn.cursor()
cur.execute(
 

#  """ 
#  create table if not exists tasks(
#  id integer primary key autoincrement,
#  title text,
#  assign text,
#  status text,
#  comment text
#  )


#  """






""" 
create table if not exists feedback(
fid integer primary key autoincrement,
name text,
mobile text,
salary integer,
created_date text,
comment text
)


"""
)


# print message
print("Table created successfully in database")

# save query
conn.commit()
conn.close()