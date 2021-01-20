#1173.Immediate Food Delivery I
SELECT ROUND(AVG(CASE WHEN order_date = customer_pref_delivery_date
                THEN 1 ELSE 0 END) * 100, 2) AS immediate_percentage
                FROM delivery;
#It may not be the optimal solution in consideration of the potential ties.