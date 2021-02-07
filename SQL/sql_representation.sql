#sql special representation

#calculate the date difference:
#datediff(year, "2017-08-25", "2011-08-25") AS DateDiff -> 6;
#datediff(quarter, "2005-12-31 23:59:59:9999999", "2020-12-31 23:59:99:9999999") AS quarter -> 60;
#datediff(month/dayofyear/day/week/hour/minute/second/millisecond/microsecond)
#SELECT DATEDIFF(DAY, GETDATE(), GETDATE() + 1) AS DayDiff
#SELECT DATEDIFF(MINUTE, GETDATE(), GETDATE() + 1) AS MinuteDiff
#SELECT DATEDIFF(SECOND, GETDATE(), GETDATE() + 1) AS SecondDiff
#SELECT DATEDIFF(WEEK, GETDATE(), GETDATE() + 1) AS WeekDiff
#SELECT DATEDIFF(HOUR, GETDATE(), GETDATE() + 1) AS HourDiff
#(CASE WHEN C1 THEN A1 WHEN C2 THEN A2 WHEN C3 THEN A3 ELSE A4 END)
#DATE_ADD(Login_date, INTERVAL 4 DAY)
#DATE_ADD(Login_date, INTERVAL -4 DAY)
#WHERE COUNTS <> (SELECT max(COUNTS) FROM A1)
#COUNTS <> (SELECT min(COUNTS) FROM A1)
#SUM(CASE WHEN AND THEN 3 ELSE 1)
#IFNULL(SUM(CASE WHEN COND1 THEN 1 ELSE 0 END), 0) -> coalesce(0)
#NULL + 1 = NULL
#ROUND(AVG(), 2)
#