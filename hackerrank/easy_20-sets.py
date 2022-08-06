"""

-------------------- Using the update() function: ------------------------------------

>> myset.update([1, 2, 3, 4]) # update() only works for iterable objects
>> myset
{'a', 1, 'c', 'b', 4, 2, (5, 4), 3}
>> myset.update({1, 7, 8})
>> myset
{'a', 1, 'c', 'b', 4, 7, 8, 2, (5, 4), 3}
>> myset.update({1, 6}, [5, 13])
>> myset
{'a', 1, 'c', 'b', 4, 5, 6, 7, 8, 2, (5, 4), 13, 3}


---------------------- REMOVING ITEMS ------------------------------------------


Both the discard() and remove() functions take a single value as an argument and removes that value from the set. If that value is not present, discard() does nothing, but remove() will raise a KeyError exception.

>> myset.discard(10)
>> myset
{'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 13, 11, 3}
>> myset.remove(13)
>> myset
{'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 11, 3}



--------- union(), intersection() and difference() ------------

>> a = {2, 4, 5, 9}
>> b = {2, 4, 11, 12}
>> a.union(b) # Values which exist in a or b
{2, 4, 5, 9, 11, 12}
>> a.intersection(b) # Values which exist in a and b
{2, 4}
>> a.difference(b) # Values which exist in a but not in b
{9, 5}


>> a.union(b) == b.union(a)
True
>> a.intersection(b) == b.intersection(a)
True
>> a.difference(b) == b.difference(a)
False

"""


"""
Given  sets of integers print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either sets but do not exist in both.

Sample Input

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}

Sample Output

5
9
11
12
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
m_set = {int(i) for i in input().split(' ')}  # creating the first set
# print(m_set)
n = int(input())
n_set = {int(i) for i in input().split(' ')}  # creating the second set
# print(n_set)
only_in_m = m_set.difference(n_set)  # elements only in m_set but not in n_set
only_in_n = n_set.difference(m_set)  # elements only in n_set but not in m_set
for _ in sorted(only_in_m.union(only_in_n)):  # combine the two sets and then sort them
    print(_)
