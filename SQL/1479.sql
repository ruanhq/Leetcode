#1479. Sales by day of week:
#weekday(date) = 0:Monday = 6: Sunday
SELECT I.item_category AS 'CATEGORY', 
SUM(CASE WHEN weekday(O.order_date) = 0 THEN I.quantity ELSE 0 END ) AS "MONDAY",
sum(case when weekday(a.order_date) = 1 then a.quantity else 0 end) as 'TUESDAY',
sum(case when weekday(a.order_date) = 2 then a.quantity else 0 end) as 'WEDNESDAY',
sum(case when weekday(a.order_date) = 3 then a.quantity else 0 end) as 'THURSDAY',
sum(case when weekday(a.order_date) = 4 then a.quantity else 0 end) as 'FRIDAY',
sum(case when weekday(a.order_date) = 5 then a.quantity else 0 end) as 'SATURDAY',
sum(case when weekday(a.order_date) = 6 then a.quantity else 0 end) as 'SUNDAY'
FROM Items I LEFT JOIN Orders O ON I.item_id = O.item_id
GROUP BY I.item_category
ORDER BY I.item_category;