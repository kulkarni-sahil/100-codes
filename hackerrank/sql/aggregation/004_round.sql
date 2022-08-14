/*
Query the average population for all cities in CITY, rounded down to the nearest integer.

round - https://www.w3schools.com/SQl/func_sqlserver_round.asp
round(float_value, round_to_how_much)
*/

select round(avg(population), 0) from city 