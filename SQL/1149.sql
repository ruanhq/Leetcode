#1149. Article Views II
#View more than one articles in the same day.
SELECT viewer_id AS id 
FROM Views 
GROUP BY viewer_id, view_date
HAVING COUNT(DISTINCT article_id) > 1
ORDER BY 1;