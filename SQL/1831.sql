#1831. Maximum Transaction Each Day
SELECT transaction_id FROM
(
SELECT transaction_id, DENSE_RANK() OVER(PARTITION BY substring(day, 1, 10) ORDER BY amount DESC) AS drkCount
FROM Transactions
) A1
WHERE drkCount = 1
ORDER BY transaction_id ASC;
#datetime: YY-MM-DD HH-MM-SS
#date: YY-MM-DD