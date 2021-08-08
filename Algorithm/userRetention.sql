#userRetention Result

#user_log: log_day, device_id, app_id:
#primary key: device_id, app_id:

SELECT *,
ROUND(100 * userCountDayMinus1/ userCountToday, 2) || "%" AS oneDayRetentionRate,
ROUND(100 * userCountDayMinus3/ userCountToday, 2) || "%" AS threeDayRetentionRate,
ROUND(100 * userCountDayMinus7/ userCountToday, 2) || "%" AS sevenDayRetentionRate
FROM
(SELECT 
A.log_day,
COUNT(DISTINCT(A.device_id || A.app_id)) AS userCountToday,
COUNT(DISTINCT(B.device_id || B.app_id)) AS userCountDayMinus1,
COUNT(DISTINCT(C.device_id || C.app_id)) AS userCountDayMinus3,
COUNT(DISTINCT(D.device_id || D.app_id)) AS userCountDayMinus7,
COUNT(DISTINCT(E.device_id || E.app_id)) AS userCountDayMinus30
FROM user_log AS A
LEFT JOIN user_log AS B ON A.device_id || A.app_id = B.device_id || B.app_id AND A.log_day = B.log_day + 1
LEFT JOIN user_log AS C ON A.device_id || A.app_id = C.device_id || C.app_id AND A.log_day = C.log_day + 3
LEFT JOIN user_log AS D ON A.device_id || A.app_id = D.device_id || D.app_id AND A.log_day = D.log_day + 7
LEFT JOIN user_log AS E ON A.device_id || A.app_id = E.device_id || E.app_id AND A.log_day = E.log_day + 30
GROUP BY A.log_day) AS A1;


SELECT *,
ROUND(100 * userCountDayMinus1/ userCountToday, 2) || "%" AS oneDayRetentionRate,
ROUND(100 * userCountDayMinus3/ userCountToday, 2) || "%" AS oneDayRetentionRate,
ROUND(100 * userCountDayMinus7/ userCountToday, 2) || "%" AS oneDayRetentionRate
FROM
(SELECT 
A.log_day,
COUNT(DISTINCT(A.device_id || A.app_id)) AS userCountToday,
COUNT(DISTINCT(B.device_id || B.app_id)) AS userCountDayMinus1,
COUNT(DISTINCT(B.device_id || B.app_id)) AS userCountDayMinus3,
COUNT(DISTINCT(B.device_id || B.app_id)) AS userCountDayMinus7,
COUNT(DISTINCT(B.device_id || B.app_id)) AS userCountDayMinus30
FROM user_log AS A
LEFT JOIN user_log AS B ON A.device_id || A.app_id = B.device_id || B.app_id AND A.log_day = B.log_day + 1
LEFT JOIN user_log AS C ON A.device_id || A.app_id = C.device_id || C.app_id AND A.log_day = C.log_day + 3
LEFT JOIN user_log AS D ON A.device_id || A.app_id = D.device_id || D.app_id AND A.log_day = D.log_day + 7
LEFT JOIN user_log AS E ON A.device_id || A.app_id = E.device_id || E.app_id AND A.log_day = E.log_day + 30
GROUP BY A.log_day) AS A1;


"a" || "," || "b"
"a" || "," || "b"
#DATEDIFF(day, BirthDate, GETDATE()) FROM Employees;
#Get the order details from the curdate:

SELECT DATEDIFF(day, BirthDate, GETDATE()) FROM Employees;
GETDATE(): get the date of today.

#drop duplicates: 
#table: user_log
#columns: log_day, device_id, app_id
SELECT log_day, device_id, app_id 
FROM
(SELECT *, ROW_NUMBER() OVER(PARTITION BY device_id, app_id ORDER BY log_day ASC) AS deviceappRk
FROM user_log) AS A
WHERE A.deviceappRk = 1

#一个表一个主键，多个唯一索引
#适合不容易更改的唯一标识，如身份证号等。
#主键执行计划优先级高于唯一索引，可以提高查询速度。
#GETDATE(),
#row_number() OVER(partition by device_id, app_id)


SELECT DATEDIFF(day, Birthdate, GETDATE()) FROM Employees;
#索引可以提高查询速度。


#table soccer: date, result
SELECT date, COUNT(case when result = "胜" THEN result END) AS winCount,
COUNT(case when result = "负" THEN result END) AS loseCount
FROM soccer 
GROUP BY date;





#table A: course, teacher, score
#for each of the course, we define pass as more than the mean of the score:
#get the average passing score:

#Get the users who logged in for at least 7 consecutive days:
#table A: user_id, log_id, session_id, log_in_date

SELECT user_id FROM
(SELECT user_id, ROW_NUMBER() OVER(partition by user_id ORDER BY log_id DESC) AS ranks, 
log_id - ranks AS dateRankCount FROM A) 
GROUP BY user_id
HAVING COUNT(dateRankCount) >= 7

Set2 = set()
COUNT(primary key), COUNT(1)
modify column/ change column


#find the largest one:

#Gini-index versus cross-entropy:
{key: value for key, value in dic1.items() if value > k}

for key, value in dict(myDict).items():
    if value == 42:
        del myDict[key]





(SELECT country, COUNT(DISTINCT user_id) AS AA FROM Table_user
GROUP BY country) A1
SELECT country FROM (SELECT * FROM A1 ORDER BY AA DESC LIMIT 1)
UNION
SELECT country FROM (SELECT * FROM A1 ORDER BY AA ASC LIMIT 1)



(SELECT country, COUNT(DISTINCT user_id) AS AA FROM Table_user
GROUP BY country) A1







#MyCustomerTransactionTable: CustomerID, Date, Action, Amount
#MyCustomerTable: CustomerID, FirstName, MiddleName, LastName, Phone

#1.
SELECT Phone FROM MyCustomerTable WHERE Phone LIKE '%415'

#2.
SELECT Action, COUNT(*) AS actionCount
FROM MyCustomerTransactionTable GROUP BY Action
ORDER BY Action DESC;

#3.
SELECT COUNT(DISTINCT CustomerID) AS countCustomerDeposits
FROM MyCustomerTransactionTable WHERE Action = 'Deposit'

#4.
SELECT * FROM MyCustomerTransactionTable
WHERE CustomerID FROM 

(SELECT C.*,
COUNT(CASE WHEN T.Actio = 'Deposit' THEN T.CustomerID END) AS DepositCount
)


#5. 
SELECT 

FROM 
MyCustomerTransactionTable A 
JOIN 
MyCustomerTable B 
ON A.CustomerID = B.CustomerID



#5. Find the top date for withdraw amount each day 
#and its transaction information 
SELECT CustomerID, Dates, DailyNetAmount FROM 
(SELECT CustomerID, Dates, 
SUM(CASE WHEN Action = 'Deposit' THEN Amount) AS DailyDepositAmount,
SUM(CASE WHEN Action = 'Withdraw' THEN Amount) AS DailyWithdrawAmount,
(DailyDepositAmount - DailyWithdrawAmount) AS DailyNetAmount,
ROW_NUMBER() OVER (PARTITION BY CustomerID, Dates ORDER BY DailyNetAmount DESC) AS RK 
FROM MyCustomerTransactionTable
GROUP BY CustomerID, Dates) A1
WHERE A1.RK = 1
ORDER BY CustomerID DESC, Dates DESC;



#6. List the number with no transactions:
SELECT T2.CustomerID, T2.FirstName, T2.MiddleName, T2.LastName,
T2.Phone FROM 
(MyCustomerTable T2
LEFT JOIN 
(SELECT CustomerID, Action FROM MyCustomerTransactionTable WHERE Action != "Inquiry") T1
ON T2.CustomerID = T1.CustomerID) A1
WHERE T1.Action is null


#7. For each of the customer, return the date and activity of its first action:
SELECT A1.customerID, A1.Action, A2.FirstName, A2.Phone
FROM 
(SELECT customerID, Action, ROW_NUMBER() OVER(PARTITION BY customerID ORDER BY dates ASC) AS RK
FROM MyCustomerTransactionTable) A1
JOIN
MyCustomerTable A2
ON A1.CustomerID = A2.CustomerID
WHERE A1.RK = 1;

#8. average over three days:
WITH df (t, a) AS (
VALUES(1, 1),
(2, 3),
(4, 5),
(5, 6),
(2, 5),
(2, 7),
(6, 10),
(5, 8)
)
SELECT t, a, AVG(a) OVER (ORDER BY t ROWS BETWEEN 1 PRECEDING
AND 1 FOLLOWING)
FROM df
ORDER BY t

#UNBOUNDED PRECEDING: starting from scratch for this segment
#ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
#ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
#ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
#UNBOUNDED PRECEDING 
#ROW_NUMBER() OVER(PARTITION BY customerID ORDER BY dates ASC) AS RK

















