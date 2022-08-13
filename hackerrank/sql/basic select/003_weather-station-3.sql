/*
Query a list of CITY names from STATION for cities that have an even ID number. 
Print the results in any order, but exclude duplicates from the answer.

https://tableplus.com/blog/2019/09/select-rows-odd-even-value.html#:~:text=Syntax,otherwise%2C%20that's%20an%20odd%20number.
mod(column_name, divisor)

DISTINCT - unique values

*/

select distinct city from station where mod(id, 2) = 0;
