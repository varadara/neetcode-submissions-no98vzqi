-- Write your query below
select employee_id,
case when name not like 'M%' then
salary * (employee_id % 2)
else 0 end bonus
from employees
order by employee_id asc