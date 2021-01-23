#1501. Countries you can safely invest in 
with ps as (
    select p.*, c.name as country from person p
    left join country c on c.country_code = substring(p.phone_number, 1, 3)
),
call as(
    select caller_id, duration from calls
    union all
    select callee_id, duration from calls
),
cntry as(
    select ps.country, avg(c.duration) as avgd from call c
    left join ps on ps.id = c.caller_id
    group by ps.country
)
select country from cntry
where avgd > (select avg(duration) from calls)