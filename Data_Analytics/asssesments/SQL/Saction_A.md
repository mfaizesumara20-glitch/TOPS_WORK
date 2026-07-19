1. You are setting up a new database for the Zomato project. Which SQL command creates a new database called analytics_db?

***
CREATE DATABASE analytics_db
***

2. You add a restaurant_id column to the restaurants table as its primary key. What is a primary key, and why must its values be unique?

***
A Primary Key is a column that uniquely identifies each row in a table.
***
***

It cannot contain duplicate values.
***


***


It cannot contain NULL values.
***


***


It ensures that every record has a unique identity.

***



3. The ratings table references restaurant_id from the restaurants table. What is a foreign key, and what integrity rule does it enforce?

***
A Foreign Key is a column in one table that refers to the Primary Key of another table.
***
***
It enforces Referential Integrity, which means:
***
***
Every foreign key value must already exist in the referenced primary key table.
***
***
It prevents invalid records.
***


4. You apply a NOT NULL constraint to the restaurant_name column. What kind of data entry does this constraint prevent?

***
The NOT NULL constraint prevents users from inserting or updating a row without a value for the restaurant_name column.
***

