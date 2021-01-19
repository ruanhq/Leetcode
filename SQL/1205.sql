#Monthly Transactions II:
#Using the middle table:
WITH A1 AS
(
SELECT id, country, amount, state, substring(trans_date, 1, 7) AS month FROM Transactions WHERE state = "approved"
UNION
(
SELECT C.trans_id, T.country, T.amount, 'chargeback' as state, substring(C.trans_date, 1, 7) AS month
FROM Chargebacks C JOIN 
    Transactions T ON C.trans_id = T.id
)
)
SELECT month, country, sum(case when state='approved' then 1 else 0 end) as approved_count, 
sum(case when state='approved' then amount else 0 end) as approved_amount, 
sum(case when state='chargeback' then 1 else 0 end) as chargeback_count, 
sum(case when state='chargeback' then amount else 0 end) as chargeback_amount
FROM A1
GROUP BY month, country
ORDER BY month

