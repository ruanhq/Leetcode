#1045. Customers who bought all products:

SELECT customer_id FROM
(
SELECT customer_id, COUNT(DISTINCT product_key) as count_product_key
FROM Customer
GROUP BY customer_id
HAVING count_product_key = (SELECT COUNT(DISTINCT product_key) FROM Product)
) AS A1;