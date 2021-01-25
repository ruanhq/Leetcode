#1549. The most recent orders for each product:
WITH A1 AS(
SELECT product_name, P.product_id, order_id, order_date, DENSE_RANK() OVER (PARTITION BY product_name ORDER BY order_date DESC) AS RK
    FROM Orders O JOIN Products P
    ON O.product_id = P.product_id
)
SELECT product_name, product_id, order_id, order_date
FROM A1 WHERE RK = 1
ORDER BY product_name ASC, product_id ASC, order_id ASC;