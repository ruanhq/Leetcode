#1555
SELECT user_id,
       user_name,
       (credit - coalesce(out_amnt, 0) + IFNULL(in_amnt, 0)) AS credit,
       IF((credit - coalesce(out_amnt, 0) + IFNULL(in_amnt, 0)) < 0, 'Yes', 'No') AS credit_limit_breached
FROM Users U
LEFT JOIN
    (SELECT paid_by,
            SUM(amount) AS out_amnt
     FROM Transactions
     GROUP BY paid_by) out_tmp
ON U.user_id = out_tmp.paid_by
LEFT JOIN
    (SELECT paid_to,
            SUM(amount) AS in_amnt
     FROM Transactions
     GROUP BY paid_to) in_tmp 
ON U.user_id = in_tmp.paid_to