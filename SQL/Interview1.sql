#SQL: Composer, table composer, 3 columns: userid, event, date,
#
#

SELECT date, 
ROUND(IFNULL(SUM(CASE WHEN event = 'post' THEN 1 ELSE 0 END)/
SUM(CASE WHEN event = 'enter' THEN 1 ELSE 0 END), 0), 2) AS success_date
FROM composer WHERE DATEDIFF(CURDATE(), date) <= 7
GROUP BY date;

table2: user: userid | date| country |dau_flag{0, 1}

SELECT country,
ROUND(IFNULL(SUM(CASE WHEN event = 'post' THEN 1
ELSE 0 END)/COUNT(DISTINCT U.user_id), 0), 2) AS avg_posts)
FROM
user U LEFT JOIN Composer C
ON U.userid = C.userid AND U.date = C.date
WHERE date = CURDATE() AND U.dau_flag = 1
GROUP BY country;


SELECT country,
ROUND(IFNULL(s))

#ds(date, String) | user_id | post_id | action ('view', 'like', 'reaction', '') | extra(extra reason for the action, e.g. 'love', 'spam', 'nudity')
#Table: user_actions:

SELECT extra AS reason, COUNT(DISTINCT postid)
FROM user_actions 
WHERE action = 'report' AND DATEDIFF(CURDATE(), date) = 1
GROUP BY reason/ 1;

#review_removals: ds(date, String) | review_id | post_id

SELECT U.date, U.user_id,
COUNT(review_id)/COUNT(DISTINCT U.post_id) AS percentage
FROM user_actions U 
LEFT JOIN 
review_removals R 
ON U.post_id = R.post_id
GROUP BY U.date, U.user_id;


#session level data:
#(user, group, time, displays, click) for a payment page.
#(1): 
#(2): click through rate:
SELECT U.date, U.user_id,
COUNT(DISTINCT review_id)/ COUNT(DISTINCT U.post_id) AS percentage
FROM user_actions U
LEFT JOIN 
review_removals R 
ON U.post_id = R.post_id 
GROUP BY 1, 2;

#What's the sample with most frequent one? LIMIT 1;










