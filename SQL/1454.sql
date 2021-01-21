#1454: Active Users: With at least 5 consecutive days
WITH t AS (
    SELECT DISTINCT id, login_date, DENSE_RANK() OVER (PARTITION BY id ORDER BY login_date) rank_date
FROM Logins
)

SELECT id, name 
FROM Accounts a
WHERE id IN (
    SELECT t1.id 
    FROM t t1, t t2
    WHERE t1.login_date = DATE_ADD(t2.login_date, INTERVAL 4 DAY) 
    AND t1.rank_date - t2.rank_date = 4
    AND t1.id = t2.id)
ORDER BY 1