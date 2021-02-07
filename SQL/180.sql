#180.sql
#Methodology1:
SELECT DISTINCT Num AS ConsecutiveNums FROM 
(SELECT Num, lead(Num, 1) OVER (ORDER BY Id) AS Id1, lead(Num, 2) OVER (ORDER BY Id) AS Id2
FROM Logs) A
WHERE A.Id1 = A.Num AND A.Id2 = A.Id1;

#Methodlogy2:
SELECT DISTINCT Num AS ConsecutiveNums FROM
Logs L1, Logs L2, Logs L3
WHERE L1.Id = L2.Id - 1 AND L2.Id = L3.Id - 1
AND L1.Num = L2.Num AND L2.Num = L3.Num;

