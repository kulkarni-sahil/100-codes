/*
Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

where city not rlike '^[aeiouAEIOU]'
*/

SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY NOT RLIKE '^[aeiouAEIOU]'