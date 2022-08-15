/*
join the two tables on country code and then filter on continent as asia and do sum on population
*/
select sum(city.population) from city left join country on city.countrycode = country.code where country.continent = 'Asia'