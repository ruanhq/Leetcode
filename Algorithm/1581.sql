#1581. Customer who visited but did not make any transactions
SELECT customer_id, COUNT(DISTINCT visit_id) FROM 
(
SELECT customer_id, Visits.visit_id
FROM 
Visits LEFT JOIN 
Transactions ON
Visits.visit_id = Transactions.visit_id
) A1
GROUP BY customer_id
ORDER BY customer_id ASC;

