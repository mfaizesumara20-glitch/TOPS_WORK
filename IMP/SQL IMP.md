# Difference Between WHERE and HAVING
  ***
WHERE filters rows before grouping and aggregation.
HAVING filters groups after GROUP BY and aggregation.
Example Using WHERE

Show orders where the amount is greater than 500:

SELECT *
FROM Orders
WHERE amount > 500;

Here, WHERE filters individual rows (orders).

Example Using HAVING

Show payment methods whose average order amount is greater than 500:

SELECT payment_method,
       AVG(amount) AS avg_amount
FROM Orders
GROUP BY payment_method
HAVING AVG(amount) > 500;

Here, HAVING filters groups (payment methods) after calculating the average.


***
