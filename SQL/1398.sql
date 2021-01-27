#1398. Customers Who bought products A, B but not C
SELECT C.customer_id, C.customer_name
FROM Customers C, Orders O
WHERE C.customer_id = O.customer_id
GROUP BY C.customer_id
HAVING SUM(O.product_name = "A") > 0 AND 
SUM(O.product_name = "B") > 0 AND 
SUM(O.product_name = "C") = 0;