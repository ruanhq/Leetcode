#1543.sql:

SELECT lower(trim(product_name)), sale_date, COUNT(sale_date) AS total
FROM
(
SELECT DISTINCT sale_id, product_name, substring(sale_date, 1, 7) AS sale_date 
    FROM Sales
)AS A
GROUP BY 1, 2
ORDER BY 1 ASC, 2 ASC;


#date_format(sale_date, "%Y-%m") AS sale_date
#date_format(sale_date, "%Y-%m") AS sale_date

select lower(trim(product_name)), sale_date, COUNT(sale_date) AS total
FROM 
(
SELECT DISTINCT sale_id, product_name, substring(sale_date, 1, 7) AS sale_date
FROM Sales
) AS A 
GROUP BY 1, 2
ORDER BY 1 ASC, 2 ASC;


################



