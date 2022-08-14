/*
Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's  key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

Write a query calculating the amount of error (i.e.: actual - miscalculated average monthly salaries), and round it up to the next integer.

============================================================================

replace method is working with integer as well!!! - very interesting
https://www.w3schools.com/sql/func_sqlserver_replace.asp
replace(salary, '0', '') -> replaces 0 with empty thing

ceil -> rounds up the calculation to next highest integer

*/

select ceil(avg(salary) - avg(replace(salary, '0', ''))) from employees
