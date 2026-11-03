# import pandas as pd
# import matplotlib.pyplot as plt

# data = {

#     'employee_name': ['faize','alan','alax','Karan','Arju','Rohan','Neha','Priya','Anjali','Pooja'],
#     'department' : ['IT','CSE','HR','EE','EC','IT','EE','CSE','HR','IT'],
#     'salary': [15000,16000,17000,18000,19000,20000,22000,25000,26000,30000]




# }
# df = pd.DataFrame(data)
# print(df)



# print('--------------------------------------')

# print("total salary :" , df['salary'].sum())
# print("total salary :" , df['salary'].mean())


# print('--------------------------------------')

# avrage_salary =  df['salary'].mean()


# print('details of the emplyoee having more then avg salary :', df[df['salary'] > avrage_salary])



# hi_salary = df[df['salary'] > avrage_salary]


# plt.title('highest salary')
# plt.pie(
#     hi_salary['salary'],
#     labels=df['employee_name'],
#     autopct="%1.1f%%"
# )

# plt.show()




import pandas as pd
import matplotlib.pyplot as plt

data = {

    'employee_name': [
        'faize', 'alan', 'alax', 'Karan', 'Arju',
        'Rohan', 'Neha', 'Priya', 'Anjali', 'Pooja'
    ],

    'department': [
        'IT', 'CSE', 'HR', 'EE', 'EC',
        'IT', 'EE', 'CSE', 'HR', 'IT'
    ],

    'salary': [
        15000, 16000, 17000, 18000, 19000,
        20000, 22000, 25000, 26000, 30000
    ]
}

df = pd.DataFrame(data)

print(df)

print('--------------------------------------')

print("Total salary:", df['salary'].sum())
print("Average salary:", df['salary'].mean())

print('--------------------------------------')

average_salary = df['salary'].mean()

hi_salary = df[df['salary'] > average_salary]

print(
    'Details of employees having more than average salary:'
)
print(hi_salary)

plt.title('Employees With Above Average Salary')

plt.pie(
    hi_salary['salary'],
    labels=hi_salary['employee_name'],
    autopct="%1.1f%%"
)

summery =







exel =df.to_excel('emplyee.xlsx',engine='openpyxl',index= False)

print("Data exported to employee.xlsx successfully.", exel)
plt.show()

