#Write your MySQL query statement below
SELECT W.name AS warehouse_name, SUM(P.Width * P.Length * P.Height * W.units) AS volume
FROM Warehouse AS w LEFT JOIN Products AS P ON W.product_id = P.product_id 
GROUP BY W.name;

