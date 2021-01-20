#1125:Report contiguous Dates

#Solution2:
select state as period_state, min(date1) as start_date, max(date1) as end_date
FROM
(select fail_date as date1, 'failed' as state,
Dense_rank() over(order by fail_date) as myrank
FROM Failed
UNION ALL
select success_date as date1, 'succeeded' as state,
Dense_rank() over(order by success_date) as myrank
FROM Succeeded)t
where date1 between '2019-01-01' and '2019-12-31'

group by state, date_add(date1,interval -myrank day)
order by start_date

#a column of date substract a column of number of days:date_add(date1, interval -rk day)