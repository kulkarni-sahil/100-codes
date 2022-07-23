"""

Size: 7 x 21 
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------

Size: 11 x 33
---------------.|.---------------
------------.|..|..|.------------
---------.|..|..|..|..|.---------
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
-------------WELCOME-------------
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
---------.|..|..|..|..|.---------
------------.|..|..|.------------
---------------.|.---------------

"""


import math
# Enter your code here. Read input from STDIN. Print output to STDOUT
ip = input()
ip_split = ip.split(' ')
n = int(ip_split[0])
m = int(ip_split[1])

welcome = 'WELCOME'
vertical_pattern = '.|.'
dash_pattern = '-'
matrix = []
middle_row = math.ceil(n/2)
# print(middle_row)
for row in range(1, n+1):
    # print(row)
    if row == middle_row:
        remaining_columns = int(m - len(welcome))
        pattern = dash_pattern*int((remaining_columns/2)) + welcome + dash_pattern*int((remaining_columns/2))
        matrix.append(pattern)
    else:
        # print(middle_row - int(abs(middle_row-row)))
        no_of_vertical_patterns_needed = middle_row - int(abs(middle_row-row)) - 1
        vertical_design = vertical_pattern * no_of_vertical_patterns_needed * 2 + vertical_pattern
        # print(vertical_design)
        remaining_columns = int(m - len(vertical_design))      
        pattern = dash_pattern*int((remaining_columns/2)) + vertical_design + dash_pattern*int((remaining_columns/2))  
        matrix.append(pattern)
        
    # print(matrix)
        
for p in matrix:
    print(p)
            
