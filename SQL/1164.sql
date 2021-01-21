#1164:Product Price at a Given Date

WITH A1 AS (
    SELECT product_id, MAX(change_date) as max_change_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)
SELECT p.product_id, new_price as price
FROM Products p
JOIN A1 m ON m.product_id = p.product_id AND p.change_date = m.max_change_date
UNION ALL
SELECT DISTINCT product_id, 10 as price
FROM Products
WHERE product_id NOT IN (SELECT product_id FROM A1)



