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

#calculate the count of interactions of each friend

select t1.user1, t1.user2, count(t2.sender) as pair_total_interaction
from friend_pair t1 
left join interaction t2
ON t1.user1 = t2.sender and t1.user2 = 

#request table - (sender_id, send_to_id, time)
#accept table - (requester_id, accepter_id, time)

select count(A.request_id)/count(R.sender_id) as acceptance_rate
from request R, accept A
where
date(R.time) = 'XXX' and date(A.date) = 'XXX';

#different writing in sql and scala.
date(R.time) = "XXX"




#Qualification fraud: KYC
#1. register address fraud -> shared with blacklist; rules to block
#2. shared email address
#3. shared email, shared email --> fraudulent behaviors.



select songid, count(distinct user_id) as num 
from table1 
where date(time) = curdate()
group by 1
order by 2 desc
limit 1;

group by 1 
order by 2 desc 
limit 1;

select question_id, sum(case when event = 'answered' then 1 else 0 end)/
sum(case when event = 'imp' then 1 else 0 end) as answer_rate
from survey_log
group by 1 
order by 2 desc
limit 1;

select question_id, sum(case when 
event = 'answered' then 1 else 0 end)/
sum(case when event = 'imp' then 1 else 0 end) as answer_rate
from survey_log 
group by 1
order by 2 desc 
limit 1;


select count(distinct a.request_id)/ count(distinct r.sender_id) as 
acceptance_rate\
from request r,
accept a
where date(r.time) = date(a.time)



select request_id as user_id, accepter_id as applier_id

#working with session level data:
#intensive usage of window functions:
#date, country, cell_number, carrier, type
#date, cell_number
datediff(curdate(), date) = 1

select country, count(*)
from sms_message
where type = 'confirmation' and datediff(curdate(), date) = 1
group by 1 
order by 2 desc;

select date, count(distinct cell_numubers) as num_users
from sms_message
where datediff(curdate(), date) <= 7 and type = 'notification'
group by 1;


#How to detect spam review?



















