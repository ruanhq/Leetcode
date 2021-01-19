#1126:Active business:
#
WITH T1 AS
(
SELECT event_type, avg(occurences) AS AVG_OCCUR
FROM Events GROUP BY event_type
)
SELECT EE.business_id

FROM events AS EE
JOIN T1 
ON 
EE.event_type = T1.event_type
AND EE.occurences > T1.AVG_OCCUR
GROUP BY EE.business_id
HAVING COUNT(*) > 1;