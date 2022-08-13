"""

from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i

o/p:
('python', ['awesome', 'language'])
('something-else', ['not relevant'])

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = (int(i) for i in input().split(' '))
n_list = []
for _ in range(n):
    n_list.append(input())

# This Section is Important
from collections import defaultdict
n_d = defaultdict(list)
for i in range(len(n_list)):
    n_d[n_list[i]].append(str(i+1))

m_list = []
for _ in range(m):
    x = input()
    print(' '.join(n_d[x])) if n_d[x] else print(-1)
