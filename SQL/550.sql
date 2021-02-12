#550. Game Play Analysis IV: Self-joining
#fraction of players logged in again on the day after the day they
#first logged in:
SELECT ROUND(COUNT(A2.player_id) / COUNT(A1.player_id), 2) AS fraction
FROM 
(SELECT player_id, MIN(event_date) AS first_login FROM Activity
GROUP BY player_id) A1
LEFT JOIN Activity AS A2 
ON A1.player_id = A2.player_id AND
A1.first_login = A2.first_login - 1;
#self join:FROM Activity A1, Activity A2
#WHERE A1. = A2. 
#ROUND(COUNT(A2.player_id) / COUNT(A1.player_id), 2) AS fraction
#FROM (SELECT player_id, MIN(event_date))