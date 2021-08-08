#1. ownership in your area
#2. show leadership, develop the strategy and have an impact
#3. Core mission is to make an impact on real people through our technology.
#Upstart's mission really that's exactly what I'm going to implement in my daily work. 


#Table A: columns: user_id, action("on"/ "off"), date, time
#date_add(curdate(), interval -1 day);
#date_sub(curdate(), interval 1 day);
#where date between date_sub(CURDATE(), interval -7 day) AND CURDATE()
select count(distinct user_id) FROM A
WHERE action = "on" AND date BETWEEN date_sub(CURDATE(), interval -7 day) AND CURDATE()

select count(distinct user_id) FROM A 
where action = 'on'


#create series: generate_series(1, 200)
#generate_series("2021-01-01", "2021-04-02")
WITH numbers AS (
    SELECT * 
    FROM generate_series(1, 200)
)
SELECT generate_series * random()
FROM numbers;

generate_series(1, 200)
generate_series("2021-01-01", "2021-04-02")
SELECT comment_count,
count(distinct content_id) AS comment_post_count
FROM 
(
SELECT A.content_id, count(distinct B.content_id) AS comment_count
FROM Table A 
LEFT JOIN Table B
ON A.comment_id = B.target_id 
AND A.target_id is NULL 
AND B.target_id is not null
group by 1
)
group by comment_count
order by comment_count;

####
#Table B: content_id, content_type, target_id -> comment distribution
#post -> target is Null
#target_id is the content_id of post
#comment_type: comment/ post
SELECT comment_count, 
count(distinct content_id) AS comment_post_count
FROM
(SELECT A.content_id, count(distinct B.content_id) AS comment_count
FROM Table A 
LEFT JOIN Table B
ON A.comment_id = B.target_id
AND A.target_id IS NULL 
AND B.target_id IS NOT NULL 
GROUP BY 1)
GROUP BY comment_count
ORDER BY comment_count



####
#Table C:
#time, user_id, app, event(impression, click)
#time || user_id || app || event
#select count(distinct case when B.price > 0 THEN A.Advertiser_id END)/ count(distinct A.Advertiser_id) AS PCTG_conversion
#FROM Adv_info A JOIN Ad_info B ON A.ad_id = B.ad_id
#select count(distinct case when B.price > 0 THEN A.Advertiser_id END)/ count(distinct A.Advertiser_id) AS PCTG_conversion
#CURDATE() - 1 = A.date
#A.status = 'on'

select round(count(t2.player_id)/ count(t1.player_id), 2) AS fraction
from 
(
select player_id, min(event_date) as first_login from Activity GROUP BY player_id
) T1 
LEFT JOIN 
Activity T2 
on T1.player_id = T2.player_id AND T1.first_login = T2.event_date - 1



















