/*
Consider (a,c) and (b,d) to be two points on a 2D plane where  are the respective minimum and maximum values of Northern Latitude (LAT_N) and  are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.

Query the Euclidean Distance between points p1 and p2 and format your answer to display  decimal digits.
*/

select round(
    (
        sqrt(
            power((max(lat_n) - min(lat_n)), 2) 
            + 
            power((max(long_w) - min(long_w)), 2)
        )
    )
    , 
    4
) from station