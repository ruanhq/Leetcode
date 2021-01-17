#write your MySQL query statement below

SELECT user_id AS buyer_id, join_date, ifnull(sum(case when substring(order_date, 1, 4) = '2019' then 1 else 0 end), 0) AS orders_in_2019
FROM Users AS U JOIN Orders AS O 
ON U.user_id = O.buyer_id
GROUP BY user_id;

#IFNULL, NULL + 1 = NULL