/*
Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. 
Your result cannot contain duplicates.

where city regexp '^[aeiouAEIOU]'
*/

SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[aeiouAEIOU]';