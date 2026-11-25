import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age":[25, 30, 35, 40, 45],
    "salary":[50000, 60000, 70000, 80000, 90000]
}

df=pd.DataFrame(data)
print(df)

#find the max salary
max_salary=df['salary'].max()
print("Max Salary:", max_salary)

#find the min salary
min_salary=df['salary'].min()
print("Min Salary:", min_salary)

#find the average salary
average_salary=df['salary'].mean()
print("Average Salary:", average_salary)

#find the sum of salary
total_salary=df['salary'].sum()
print("Total Salary:", total_salary)

print(type(df))

