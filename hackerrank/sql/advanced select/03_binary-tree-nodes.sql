/*
You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.

Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

Root: If node is root node.
Leaf: If node is leaf node.
Inner: If node is neither root nor leaf node.
Sample Input


Sample Output

1 Leaf
2 Inner
3 Leaf
5 Root
6 Leaf
8 Inner
9 Leaf

case: https://www.w3schools.com/sql/sql_case.asp

if - https://www.w3schools.com/sql/func_mysql_if.asp
if (condition, "value if true", "value if false")

*/

SELECT n,
CASE
    when p is null then "Root"
    when n in (select distinct p from bst) then "Inner"
    else "Leaf"
end
FROM   bst  order by n



-- SELECT n,
--        IF(
--            p IS NULL, 
--            "Root", 
--            IF(
--                n in (select distinct p from bst), 
--                "Inner", 
--                "Leaf"
--            )           
--        )
-- FROM   bst  order by n
