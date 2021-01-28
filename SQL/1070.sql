#1070. Product Sales Analysis III:
SELECT P.product_id, S1.first_year, S1.quantity, S1.price FROM
(SELECT product_id, year AS first_year, quantity, price, DENSE_RANK() OVER(PARTITION BY product_id ORDER BY year) AS rk
FROM Sales) S1
RIGHT JOIN Product P ON S1.product_id = P.product_id
WHERE rk = 1

#Notes: USING dense_rank() here as there maybe ties and we want all those in the first year tie.