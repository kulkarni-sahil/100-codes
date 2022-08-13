/*
Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name).
If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
*/

select city, length(city) as city_length 
from station 
order by city_length desc, city asc 
limit 1;

select city, length(city) as city_length 
from station 
order by city_length asc, city asc 
limit 1;
