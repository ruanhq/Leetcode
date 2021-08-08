#626. Exchange Seats:


#Current date minus

DATE_ADD(BIRTHDATE, INTERVAL 29 DAY),
BIRTHDATE,
DATE_SUB(BIRTHDATE, INTERVAL 29 DAY)
DATE_SUB(BIRTHDATE, INTERVAL 29 MONTH)


SELECT IFNULL(ROUND(COUNT(DISTINCT session_id)/ COUNT(DISTINCT user_id), 2), 0) AS 
average_sessions_per_user
FROM Activity WHERE activity_date BETWEEN DATE_SUB("2019-07-27", INTERVAL 29 DAY) AND "2019-07-27"