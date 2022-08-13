/*
Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.

count(city) - count(distinct(city))

*/

select count(city) - count(distinct(city)) from station
