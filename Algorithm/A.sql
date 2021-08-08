#A: passenger_id, order_id
#B: order_id, date:
#统计每天订单量最多的用户的passenger_id以及他的订单数
SELECT passenger_id, orderCountDaily FROM 
(SELECT date, passenger_id, ROW_NUMBER() OVER(PARTITION BY date ORDER BY orderCountDaily DESC) AS rk
(SELECT date, passenger_id, count(DISTINCT order_id) AS orderCountDaily
FROM
A
RIGHT JOIN B
ON A.order_id = B.order_id
GROUP BY passenger_id, date) A1) A2
WHERE rk = 1
