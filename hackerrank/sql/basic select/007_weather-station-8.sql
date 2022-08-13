/*
Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. 
Your result cannot contain duplicates.

where city regex '^[aeiouAEIOU]' and city regex '[aeiouAEIOU]$'

*/

select distinct city from station where city regexp '^[aeiouAEIOU]' and city regexp '[aeiouAEIOU]$'