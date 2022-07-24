"""

ip:
1 2
3 4

op:
(1, 3) (1, 4) (2, 3) (2, 4)

"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]

import itertools

op_list = [str(i) for i in itertools.product(l1, l2)]
print(' '.join(op_list))
