#615. Average Salary: Departments VS Company
select department_salary.pay_month, department_id,
case
  when department_avg>company_avg then 'higher'
  when department_avg<company_avg then 'lower'
  else 'same'
end as comparison
from
(
  select department_id, avg(amount) as department_avg, date_format(pay_date, '%Y-%m') as pay_month
  from salary join employee on salary.employee_id = employee.employee_id
  group by department_id, pay_month
) as department_salary
join
(
  select avg(amount) as company_avg,  date_format(pay_date, '%Y-%m') as pay_month from salary group by date_format(pay_date, '%Y-%m')
) as company_salary
on department_salary.pay_month = company_salary.pay_month
;
#First use with to generate the intermediate tables and then merge them in
#one query.



SELECT
    department_salary.pay_month,
    department_id,
    case
        WHEN department_avg > company_avg THEN 'higher'
        WHEN department_avg < company_avg THEN 'lower'
        ELSE 'same'
    END AS comparison
FROM 