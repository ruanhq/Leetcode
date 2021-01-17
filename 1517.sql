#Write your MySQL query statement below:
SELECT user_id FROM Users
WHERE mail regexp '^[A-Za-z][A-Za-z0-9\_\.\-]*@leetcode\.com$';

