#1141: User Activity For the past 30 days I
SELECT activity_date as day, count(distinct user_id) AS active_users
FROM Activity
WHERE datediff('2019-07-27', activity_date) < 30 AND activity_type IS NOT NULL
GROUP BY activity_date;