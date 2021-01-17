#Write your MySQL query statement below:
SELECT * FROM 
Users
WHERE mail regexp '^[A-Za-z][A-Za-z0-9\_\.\-]*@leetcode\.com$';
#^: Start of string or start of line depending on multiline mode(but
#when inside brackets, it means not)
#regexp: satisfy some conditions: *: just that character in [] *[]
#+ : 1 or more preceding pattern
#^[A-Za-z]