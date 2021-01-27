#1596. The Most Frequently Ordered Products for each customer
WITH A1 AS (
SELECT O.customer_id, O.product_id, P.product_name, 
RANK() OVER (PARTITION BY customer_id ORDER BY COUNT(O.product_id) DESC) AS ranks
FROM Orders O JOIN Products P 
ON O.product_id = P.product_id
    GROUP BY customer_id, product_id
)
SELECT customer_id, product_id, product_name 
FROM A1 WHERE ranks = 1;