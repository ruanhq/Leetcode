#1747. Leetflex Banned Accounts:
SELECT A.account_id AS account_id FROM 
LogInfo A, LogInfo B
WHERE 
A.login BETWEEN B.login AND B.logout
AND A.account_id = B.account_id
AND A.ip_address != B.ip_address;





