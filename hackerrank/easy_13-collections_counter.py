"""
A counter is a container that stores elements as dictionary keys, 
and their counts are stored as dictionary values.

>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]


Counter subtract() method is used to subtract element counts from another counter. 
update() method is used to add counts from another counter.


counter = Counter('ababab')
print(counter)  # Counter({'a': 3, 'b': 3})
c = Counter('abc')
print(c)  # Counter({'a': 1, 'b': 1, 'c': 1})

# subtract
counter.subtract(c)
print(counter)  # Counter({'a': 2, 'b': 2, 'c': -1})

# update
counter.update(c)
print(counter)  # Counter({'a': 3, 'b': 3, 'c': 0})



"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

# 10
no_of_shoes = int(input()) 
# print(no_of_shoes)

# 2 3 4 5 6 8 7 6 5 18
# Counter({'5': 2, '6': 2, '2': 1, '3': 1, '4': 1, '8': 1, '7': 1, '18': 1})
raw_size_ip = input()
# print(raw_size_ip)
parsed_show_sizes_ip = [int(i) for i in raw_size_ip.split(' ')]
# print(parsed_show_sizes_ip)
shoe_sizes_to_count_map = Counter(parsed_show_sizes_ip)
shoe_sizes_key = shoe_sizes_to_count_map.keys()
no_of_custs = int(input())

earnings = 0

for _ in range(no_of_custs):
    req = [int(i) for i in input().split(' ')]
    req_shoe_size = req[0]
    payment = req[1]
    if req_shoe_size in shoe_sizes_key:
        size_count = shoe_sizes_to_count_map[req_shoe_size]
        if size_count > 0:
            earnings += payment
            shoe_sizes_to_count_map[req_shoe_size] = size_count - 1
            
print(earnings)
