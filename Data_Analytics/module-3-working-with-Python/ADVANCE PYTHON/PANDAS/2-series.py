# series is an inbuild method in python used by pandas 
# series is used to provide data of a single column in a data frame
import pandas as pd
# age=[25, 30, 35, 40, 45]
# chk=pd.Series(age)
# print(chk)

data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age":[25, 30, 35, 40, 45],
    "salary":[50000, 60000, 70000, 80000, 90000]
}

df=pd.DataFrame(data)
print(df)
chk=pd.Series(data)
print(chk)