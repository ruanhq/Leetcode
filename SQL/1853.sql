#1853. Convert Date Format:

select
CONCAT(DATENAME(WEEKDAY, day), ', ', DATENAME(MONTH, day),
', ', DATENAME(DAY, day), ', ', year(day)) AS day
FROM days

DATENAME function returns the name of date(month, day, year)
