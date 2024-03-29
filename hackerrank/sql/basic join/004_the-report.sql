/*
You are given two tables: Students and Grades. Students contains three columns ID, Name and Marks.

Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. 
Ketty doesn't want the NAMES of those students who received a grade lower than 8. 
The report must be in descending order by grade -- i.e. higher grades are entered first. 
If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. 
Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order. 
If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.

*/

select name, grade, marks from
(select name, (select grade from grades where marks between min_mark and max_mark) as grade, marks from students) student_grades
where grade > 7 order by grade desc, name asc;

select "NULL", grade, marks from
(select name, (select grade from grades where marks between min_mark and max_mark) as grade, marks from students) student_grades
where grade < 8 order by grade desc, marks asc;


/*

SELECT CASE
    WHEN G.grade > 7 THEN S.name
    ELSE NULL
    end AS names,
    G.grade,
    S.marks
FROM   students S
    JOIN grades G
    ON S.marks BETWEEN G.min_mark AND G.max_mark
ORDER  BY G.grade DESC,
    names ASC,
    S.marks ASC;

*/
