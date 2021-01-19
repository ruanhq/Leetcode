#614.Second Degree Follower
#write a query to get the amount of each follower's follower if he/she has one:
SELECT followee AS follower,
COUNT(DISTINCT follower) AS num FROM follow
 WHERE followee IN
 (
     SELECT DISTINCT follower FROM follow
)
GROUP BY 1
ORDER BY 1
