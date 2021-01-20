#1715: Count Apples and Oranges

WITH A1 AS (
(SELECT B.box_id, C.chest_id, C.apple_count, C.orange_count
FROM 
Boxes JOIN Chests 
ON Boxes.chest_id = Chests.chest_id)

UNION
SELECT * FROM Boxes
)

SELECT SUM(apple_count) AS apple_count, SUM(orange_count) AS orange_count
FROM A1;

#
select sum(apple_count) as apple_count, sum(orange_count) as orange_count from 
((select sum(c.apple_count) as apple_count, sum(c.orange_count) as orange_count from boxes b left join chests c on b.chest_id = c.chest_id where b.chest_id is not null)
union
(select sum(b.apple_count) as apple_count, sum(b.orange_count) as orange_count from boxes b)) 
as temp