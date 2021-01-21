#1532. The most recent three orders
WITH A1 AS(
SELECT row_number() OVER(PARTITION BY C.customer_id ORDER BY O.order_date DESC) AS rk, C.customer_id, C.name AS customer_name, O.order_id, O.order_date
    FROM Customers C JOIN Orders O ON C.customer_id = O.customer_id)
    
SELECT customer_name, customer_id, order_id, order_date
FROM A1 WHERE rk <= 3
ORDER BY customer_name ASC, customer_id ASC, order_date DESC;