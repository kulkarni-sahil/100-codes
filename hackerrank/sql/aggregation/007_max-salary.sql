/*

We define an employee's total earnings to be their monthly salary * months worked, 
and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. 
Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. 
Then print these values as  space-separated integers.

create new table with earnings
group by earnings
oder by earnings desc 
limit 1
select the earnings and count of employee_id

*/

select earnings, count(employee_id) from 
(select *, (salary * months) as earnings from employee) earnings_table
group by earnings order by earnings desc limit 1
