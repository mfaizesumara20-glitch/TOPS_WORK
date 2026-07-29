
### Basics (1–10)

1. What is SQL, and what is it used for?
ans-SQL (Structured Query Language) is a standardized programming language used for managing and manipulating relational databases.
It allows users to create, read, update, and delete data efficiently.


2. What is the difference between `DELETE`, `DROP`, and `TRUNCATE`?
ans- `DELETE` is a function that helps you to delete a specific column in a table.
`DROP` drop is used to delete the entire database or a datatable at once.
`TRUNCATE` is used to clear out all the data inside a table remamber only the data will be deleted the table will still exist


3. Write a query to display all records from a table named `Students`.
ans-select * from Students


4. Write a query to display only the `Name` and `Age` columns from the `Students` table.
ans-select age,Name from Students


5. How do you use the `WHERE` clause? Give an example.
ans-The WHERE clause is used to filter records. It returns only the rows that satisfy a specified condition.
   ex- select * from Students where Name=Faize


6. Write a query to display students whose age is greater than 18.
ans-select * from Students where Age>18


7. What is the purpose of the `ORDER BY` clause?
ans-`ORDER BY` is use to arrange the data into ascending or descending order 


8. Write a query to display students sorted by `Marks` in descending order.
Ans-select * from Students order by Marks desc


9. What is the difference between `DISTINCT` and `GROUP BY`?
ans-`GROUP BY` is use to group data based on columns and by applying aggregate functions.
`DISTINCT` is used to display unique values from a column by removing duplicates.


10. Write a query to display unique city names from a `Students` table.
ans-select distinct city from Students




### Intermediate (11–20)

11. What is the difference between `PRIMARY KEY` and `FOREIGN KEY`?
ans-`PRIMARY KEY` is use only one time in a table,a primary key never returns a null value,a primary key is auto_increments
`FOREIGN KEY` can be used multiple times in a table,it provides a relationship between tow or more table.


12. Write a query to count the total number of students.
    ans-SELECT COUNT(*) FROM Students


13. Write a query to find the highest salary from an `Employees` table.
ans-select * from Employees order by salary desc limit 1:


14. Write a query to calculate the average marks of students.
ans-select avg(marks) from Students
15. Explain the use of the `LIKE` operator with examples.
ans-`LIKE` operator is use to get a specific pattern in a column using wildcards


16. Write a query to display students whose names start with `'A'`.
ans-select * from Students where name like 'A%'


17. What is the purpose of the `JOIN` clause?
ans-the purpose of `JOIN` is to link the data of two or more table and provide the data according to that


18. Explain the difference between `INNER JOIN` and `LEFT JOIN`.
ans-`INNER JOIN` returns only the rows that have matching values in both tables.
`LEFT JOIN` returns all rows from the left table and the matching rows from the right table. 
If there is no match, the columns from the right table contain NULL.


19. Write a query to display employee names along with their department names using joins.
ans-SELECT Employees.EmployeeName, Departments.DepartmentName
FROM Employees
INNER JOIN Departments
ON Employees.DepartmentID = Departments.DepartmentID


20. Write a query to find the second highest salary from an `Employees` table.
    ans-select * from Employees order by salary desc limit 1,1

