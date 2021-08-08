#SQL:
#user: userid, country
#friendRequest: date | sender_id | receiver_id | flag

SELECT COUNT(CASE WHEN flag = "TRUE" THEN sender_id ELSE END)/
COUNT(sender_id) AS tongguoRatio
FROM friendRequest
GROUP BY substring(date, 1, 7) AS month;

WITH A1 AS (
SELECT COUNT(DISTINCT user.userid) AS usreceiverCount
FROM 
(friendRequest
JOIN user 
ON A.userid = user.userid
WHERE date = CURDATE())), 
A2 AS (SELECT count(DISTINCT userid) AS USuserCount FROM user WHERE country = "US")

SELECT A1.usreceiverCount/ A2.USuserCount AS atleastOne FROM A1, A2;

WITH A1 AS (
SELECT COUNT(DISTINCT user.userid) AS usreceiverCount
FROM 
friendRequest JOIN user 
ON friendRequest.receiver_id = user.userid
WHERE friendRequest.date = CURDATE()
),
A2 AS (SELECT COUNT(DISTINCT userid) AS USuserCount FROM user WHERE country = "US")


#Message with reaction:
#TB: message_id, receiver_id, sender_id, has_reaction, date
WITH A1 AS (
SELECT DISTINCT *,
CONCAT(LEAST(receiver_id, sender_id), GREATEST(receiver_id, sender_id)) AS Pairs
FROM TB
),
A2 AS (
SELECT Pairs, SUM(has_reaction) AS reactionCount
FROM A1 
GROUP BY Pairs HAVING reactionCount >= 1),
SELECT COUNT(DISTINCT A2.Pairs)/ COUNT(DISTINCT A1.Pairs) AS ConversationRatio
FROM A1, A2

#Average days from the start of the conversation:
A3 AS (
SELECT Pairs, ROW_NUMBER() OVER(PARTITION BY Pairs ORDER BY date ASC) AS rank1,
date FROM A1),
A4 AS (
SELECT Pairs, ROW_NUMBER() OVER(PARTITION BY Pairs ORDER BY date ASC) AS rank2
FROM A1 
WHERE has_reaction = 1)
A5 AS (
SELECT T1.Pairs, T1.startDate, coalesce(T2.FirstReactionDate, T1.startDate) AS FirstReactionDate
FROM (SELECT Pairs, date AS startDate FROM A3 WHERE rank1 = 1) T1
LEFT JOIN
(SELECT Pairs, date AS FirstReactionDate FROM A4 WHERE rank2 = 1) T2
ON T1.Pairs = T2.Pairs
)
SELECT AVG(datediff(day, FirstReactionDate, startDate))

#Check whether those with reactions is more active?
WITH 
A7 AS (
SELECT Pairs, SUM(has_reaction) AS reactionCount
FROM A1 
GROUP BY Pairs HAVING reactionCount = 0)
SELECT AVG(messageCount) AS avgMessageCountWithoutReaction
FROM 
(SELECT Pairs, COUNT(DISTINCT message_id) AS messageCount
FROM TB WHERE Pairs IN (SELECT Pairs FROM A7))
####
SELECT AVG(messageCount) AS avgMessageCountWithReaction
FROM 
(SELECT Pairs, COUNT(DISTINCT message_id) AS messageCount
FROM TB WHERE Pairs IN (SELECT Pairs FROM A2))

WITH A7 AS (
SELECT Pairs, SUM(has_reaction) AS reactionCount
FROM A1
GROUP BY Pairs HAVING reactionCount = 0
)


#Table: user_id, timestamp, transaction_id
WITH A1 AS (
SELECT MONTH(timestamp) AS month, user_id
FROM Table
)
SELECT COUNT(DISTINCT A2.user_id) AS Result
FROM 
(SELECT DISTINCT user_id FROM A1
WHERE month = 12) A2
LEFT JOIN
(SELECT DISTINCT user_id FROM A1
WHERE month = 1) A3
WHERE A3.user_id is null



#average time between transaction by user:
SELECT AVG(DATEDIFF(minute, nextTimeStamp, timestamp)) AS result2
FROM 
(SELECT user_id, timestamp, 
LEAD(timestamp, 1) OVER(PARTITION BY user_id ORDER BY timestamp ASC) AS nextTimeStamp
FROM Table) A1
WHERE A1.nextTimeStamp is not null;




















