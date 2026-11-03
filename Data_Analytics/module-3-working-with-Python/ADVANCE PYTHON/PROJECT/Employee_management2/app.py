
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl as xl
import numpy as np

# Connect to the SQLite database
conn = sqlite3.connect("Employee_2.db")
print("Connected to the database successfully.")

cur = conn.cursor()

# Create all four tables
cur.executescript("""
CREATE TABLE IF NOT EXISTS Departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_name TEXT,
    location TEXT
);

CREATE TABLE IF NOT EXISTS Salaries (
    salary_id INTEGER PRIMARY KEY AUTOINCREMENT,
    basic_salary INTEGER,
    bonus INTEGER
);

CREATE TABLE IF NOT EXISTS Attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    attendance_date TEXT,
    status TEXT 
);  

CREATE TABLE IF NOT EXISTS Employees (
    eid INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    mobile TEXT,
    department_id INTEGER,
    salary_id INTEGER,
    attendance_id INTEGER,

    FOREIGN KEY (department_id)
        REFERENCES Departments(department_id),

    FOREIGN KEY (salary_id)
        REFERENCES Salaries(salary_id),

    FOREIGN KEY (attendance_id)
        REFERENCES Attendance(attendance_id)
);
""")

conn.commit()
print("All tables created successfully.")

# Insert data into Departments
cur.executemany("""
INSERT OR IGNORE INTO Departments
(department_id, department_name, location)
VALUES (?, ?, ?)
""", [
    (1, 'IT', 'Rajkot'),
    (2, 'HR', 'Ahmedabad'),
    (3, 'Finance', 'Surat'),
    (4, 'Marketing', 'Vadodara'),
    (5, 'Sales', 'Rajkot')
])

# Insert data into Salaries
cur.executemany("""
INSERT OR IGNORE INTO Salaries
(salary_id, basic_salary, bonus)
VALUES (?, ?, ?)
""", [
    (1, 30000, 5000),
    (2, 25000, 3000),
    (3, 40000, 7000),
    (4, 35000, 4000),
    (5, 28000, 2000),
    (6, 45000, 8000),
    (7, 32000, 3500),
    (8, 27000, 2500),
    (9, 38000, 6000),
    (10, 22000, 1500)
])

# Insert data into Attendance
cur.executemany("""
INSERT OR IGNORE INTO Attendance
(attendance_id, attendance_date, status)
VALUES (?, ?, ?)
""", [
    (1, '2026-10-12', 'Present'),
    (2, '2026-10-12', 'Absent'),
    (3, '2026-10-12', 'Present'),
    (4, '2026-10-12', 'Late'),
    (5, '2026-10-12', 'Present'),
    (6, '2026-10-12', 'Present'),
    (7, '2026-10-12', 'Absent'),
    (8, '2026-10-12', 'Present'),
    (9, '2026-10-12', 'Late'),
    (10, '2026-10-12', 'Present')
])

# Insert data into Employees
cur.executemany("""
INSERT OR IGNORE INTO Employees
(eid, name, mobile, department_id, salary_id, attendance_id)
VALUES (?, ?, ?, ?, ?, ?)
""", [
    (1, 'Rahul Patel', '9876543210', 1, 1, 1),
    (2, 'Priya Shah', '9876543211', 2, 2, 2),
    (3, 'Amit Joshi', '9876543212', 1, 3, 3),
    (4, 'Neha Desai', '9876543213', 3, 4, 4),
    (5, 'Karan Mehta', '9876543214', 4, 5, 5),
    (6, 'Pooja Trivedi', '9876543215', 2, 6, 6),
    (7, 'Rohan Shah', '9876543216', 5, 7, 7),
    (8, 'Anjali Patel', '9876543217', 3, 8, 8),
    (9, 'Vivek Parmar', '9876543218', 4, 9, 9),
    (10, 'Sneha Joshi', '9876543219', 5, 10, 10)
])

conn.commit()
print("Data is added successfully.")

# Join all four tables
cur.execute("""
SELECT
    Employees.name,
    Employees.mobile,
    Departments.department_name,
    Departments.location,
    Salaries.basic_salary,
    Salaries.bonus,
    Attendance.attendance_date,
    Attendance.status
FROM Employees
INNER JOIN Departments
    ON Employees.department_id = Departments.department_id
INNER JOIN Salaries
    ON Employees.salary_id = Salaries.salary_id
INNER JOIN Attendance
    ON Employees.attendance_id = Attendance.attendance_id
""")

data = cur.fetchall()

# Convert JOIN results into a DataFrame
columns = [
    "Name",
    "Mobile",
    "Department",
    "Location",
    "Basic Salary",
    "Bonus",
    "Attendance Date",
    "Status"
]

df = pd.DataFrame(data, columns=columns)

print("\nEmployee Management DataFrame:")
print(df.to_string(index=False))

# Find the employee with the highest salary
highest_salary_employee = df.loc[
    df["Basic Salary"].idxmax(),
    ["Name", "Basic Salary"]
]

print("\nEmployee with the highest salary:")
print(highest_salary_employee)

# Close the database connection
conn.close()
print("\nDatabase connection closed.")
