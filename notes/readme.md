# Python

## collections.Counter

<pre>
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
</pre>
