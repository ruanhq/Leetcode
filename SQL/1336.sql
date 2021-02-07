#1336.
WITH T AS (
SELECT ROW_NUMBER() OVER() row_num
FROM Transactions
UNION 
SELECT 0
), 
T1 as (
SELECT COUNT(transaction_date) transaction_count
FROM Visits v
LEFT JOIN Transactions t
ON v.user_id = t.user_id
AND v.visit_date = transaction_date
GROUP BY v.user_id, v.visit_date
)

SELECT row_num transactions_count, COUNT(transaction_count) visits_count
FROM T
LEFT JOIN T1
ON row_num = transaction_count
GROUP BY row_num
HAVING row_num <= (SELECT MAX(transaction_count) FROM T1)
ORDER BY row_num

