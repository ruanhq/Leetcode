#1607. Sellers with No sales
SELECT seller_name FROM 
(SELECT * FROM Orders WHERE sale_date BETWEEN "2020-01-01" AND "2020-12-31") AS O1
RIGHT OUTER JOIN 
Seller ON
O1.seller_id = Seller.seller_id
WHERE customer_id IS NULL
ORDER BY seller_name ASC;
