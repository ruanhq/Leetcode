#User Purchase Platform:
WITH A1 AS (
SELECT DISTINCT spend_date, 'desktop' AS platform FROM Spending
UNION
SELECT DISTINCT spend_date, 'mobile' AS platform FROM Spending
UNION
SELECT DISTINCT spend_date, 'both' AS platform FROM Spending
),
A2 AS (
SELECT spend_date,
user_id, 
SUM(CASE WHEN platform = 'mobile' THEN amount ELSE 0 END) AS mobile_amount,
SUM(CASE WHEN platform = 'desktop' THEN amount ELSE 0 END) AS desktop_amount
FROM Spending
GROUP BY spend_date, user_id
),
A3 AS (
SELECT spend_date, user_id,
IF(mobile_amount > 0, IF(desktop_amount > 0, 'both', 'mobile'),
'desktop') AS platform,
(mobile_amount + desktop_amount) AS amount
)
SELECT A3.spend_date,
A3.platform,
IFNULL(SUM(amount), 0) AS total_amount,
COUNT(user_id) AS total_users
FROM 
A3 LEFT JOIN A1
ON A3.platform = A1.platform AND A3.spend_date = A1.spend_date
GROUP BY spend_date, platform

SELECT
    price.col1 AS col1,
    price.col2 AS col2,
    price.col3 AS col3







