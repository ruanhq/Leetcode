#1364. Number of Trusted contacts of a customer 
SELECT 
I.invoice_id, CUS.customer_name, I.price,
COUNT(DISTINCT CON.contact_name) AS contacts_cnt,
COUNT(DISTINCT CUS2.customer_name) AS trusted_contacts_cnt
FROM 
Invoices as I JOIN 
Customers as CUS ON I.user_id = CUS.customer_id
LEFT JOIN Contacts as CON ON I.user_id = CON.user_id
LEFT JOIN Customers as CUS2 ON CUS2.email = CON.contact_email
GROUP BY I.invoice_id, CUS.customer_name, I.price 
ORDER BY I.invoice_id;
#Won't need to use WITH here!