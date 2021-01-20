#1174: Immediate Food Delivery II
#
WITH A1 AS(
SELECT delivery_id, customer_id, order_date, customer_pref_delivery_date,
    RANK() OVER (PARTITION BY customer_id ORDER BY order_date) AS rk
FROM Delivery
)
SELECT ROUND(AVG(CASE WHEN order_date = customer_pref_delivery_date
                THEN 1 ELSE 0 END) * 100, 2) AS immediate_percentage
                FROM A1
                WHERE rk = 1;