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


####

SELECT (generate_series("2018-01-01":: DATE, '2018-09-01' :: DATE,
'1D')









