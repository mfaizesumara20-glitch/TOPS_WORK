# comma separated values csv
# just like a structured data

import pandas as pd
# this reads only the first 5 rows of the csv file by default
# res = pd.read_csv("user_data_100.csv")
# print(res) 

#view first row of data start 5 rows data
# res = pd.read_csv("user_data_100.csv")
# df=res.head(10)
# print(df) 

# to read the last 5 rows of the csv file
# res = pd.read_csv("user_data_100.csv")
# df=res.tail(10)
# print(df) 

# read only 1 column of the csv file
# res = pd.read_csv("user_data_100.csv")
# df=res[["first_name"]]  # replace "column_name" with the actual column name
# print(df)

res = pd.read_csv("user_data_100.csv")
print(res)
#give row and column
print(res.shape)