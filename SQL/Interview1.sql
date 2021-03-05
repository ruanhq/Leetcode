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
#comment distribution:
#content_id, content_type(comment/post), target_id
#if comment, target_id就是post的id，如果是post则target_id为NULL
#求comment的distribution:

select num_comments, count(post_id) as num_posts
from
(
select target_id as post_id, count(*) as num_comments
from table where content_type = 'comment'
group by 1
) as T1 
group by 1;
#Calculate the distribution of comment:
#why not distinct here?
select num_comments, count(distinct post_id) as num_posts
from(
  select target_id as post_id, count(*) as num_comments
  from table 
  where content_type = 'comment'
  group by target_id 
) T1 
group by 1;

#Post type distribution: content_action: 
#user_id(content_creator_id)
#content_id
#content_type
#target_id(original content_id -> comment)
#(1) distribution of stories
#(2) content_type
#poisson distribution -> binomial distribution
#right skewed normal in the second day: 
#We take all the people who share 2 pages in day 1,
#what can be their distribution of page sharing in day 2:
#mixture of normal and a point mass at 0
#should be log-normal -> exponential nature of comments -> log of the # of comments may well follow normal distribution.
#



#select count(distinct ad_account)
#from table where date = curdate() and status = 'fraud';



#Table 1: adv_info: advertiser_id | ad_id | spend
#Table 2: ad_info: ad_id | user_id | price (assume all price column > 0):
#fraction of advertiser has at least one conversion:
#每个advertiser的平均ROI:
select count(distinct advertiser_id) / (select count(distinct advertiser_id) from adv_info)
from adv_info A 
inner join 
ad_info on ad_info.ad_id = adv_info.ad_id;

select a.advertiser_id, a.ad_id, sum(ifnull(b.price, 0))/a.spend as ad_roi
from adv_info A
inner join 
ad_info B on A.ad_id = B.ad_id
group by 1, 2;

#session table:
#date | sessionid |s userid | action 
from session where datediff(curdate(), date) <= 30
#Time table:
#date | sessionid | time_spent
select date, count(distinct sessionid)/count(distinct userid) as averageNum
group by date

#the time distribution of each user:
select userTotalTime, count(Distinct user_id) as distributionOfTotalTime
from 
(select user_id, sum(ifnull(time_spent, 0)) as userTotalTime
from Time T 
inner join session S on 
S.sessionid = T.sessionid and S.date = T.date
group by 1
) as A1 
group by 1
order by 1;




hashMap = {}
hashMap[0] = 7

#request table - (sender_id, send_to_id, time)
#accept table - (requester_id, accepter_id, time)

select count(distinct a.request_id)/count(distinct r.sender_id) as acceptance_rate
from request r, accept a 
where date(r.time) = "XXX" and date(a.time) = "XXX"

select count(distinct t2.request_id)/ count(t1.sender_id) as acceptance_rate
from (
select distinct sender_id, send_to_id
from request where date(time) = "XXX"
) T1,
(
select distinct requester_id, acceptance_id
from accept where date(time) = "XXX"
) T2


select user_id, sum(num_friends) as num_friends
from 
(select requester_id as user_id, count(distinct accepter_id) as num_friends
from accept 
group by requester_id
UNION ALL 
select accepter_id as user_id, count(distinct requester_id) as num_friends
from accept 
group by accepter_id) T1
group by user_id
order by num_friends desc
limit 1;

metrics, AAREM -> AAREM?
datediff(curdate(), date) <= 30
date(R.time) = "XXX"
t1.user_id, t1.unit_id

#ad4ad: date, user_id, event(impression, click, create_ad),
#unit_id, cost, spend
#users: user_id, country, age
select country, sum(ifnull(spend, 0)) as total_spend
from users U 
left join 
ad4ad A 
USING(user_id)
where datediff(curdate(), date) <= 30
group by country;

select country, sum(ifnull(spend, 0)) as total_spend
from users U 
left join 
ad4ad A 
USING(user_id)
where datediff(curdate(), date) <= 30
group by country;

defaultdict(list) -> d[k].append(v):


#ad_id 
select avg(tot_spend) as avg_advsr_spnt
from 
(
select adverstiser_id, sum(spend) as tot_spend
from adv_info 
group by 1
) A 
#negative binomial/ log-normal

adv_info: advertiser_id | ad_id | spend  -> each advertiser_id represent an ad.
ad_info: ad_id | user_id | price 

#Fraction of advertisers who has at least 1 conversion:
select
      count(distinct advertiser_id)/(select 
      	count(distinct advertiser_id) from adv_info)
      from adv_info JOIN ad_info ON 
      adv_info.ad_id = ad_info.ad_id;

#
select t1.advertiser_id, t1.ad_id, sum(ifnull(T2.price, 0))/t1.spend as roi_adv
from adv_info t1 left join ad_info t2 on t1.ad_id = t2.ad_id 
group by 1, 2;

#average roi for each advertisement:
select A1.advertiser_id, ROUND(IFNULL(A2.total_price/ A1.total_spend, 0), 2) as advROI
FROM
(select advertiser_id, sum(ifnull(spend, 0)) as total_spend
from adv_info group by 1) as A1
left join
(select advertiser_id, sum(ifnull(price, 0)) as total_price
from adv_info left join ad_info on
adv_info.ad_id = ad_info.ad_id) as A2 
on
A1.advertiser_id = A2.advertiser_id
















