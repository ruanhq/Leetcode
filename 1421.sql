#1421: NPV queries
SELECT q.id, q.year, coalesce(n.npv, 0) as npv
FROM npv as n right join Queries q
on n.id = q.id and n.year = q.year;

#Coalesce helps you to replace null by 0.