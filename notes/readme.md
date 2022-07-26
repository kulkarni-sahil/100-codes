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

## collections.defaultdict

The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.

<pre>
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
</pre>

## itertools.permutations(iterable[, r])

This tool returns successive  length permutations of elements in an iterable.

If  is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

<pre>
>>> from itertools import permutations
>>> print permutations(['1','2','3'])
<itertools.permutations object at 0x02A45210>
>>> 
>>> print list(permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
>>> 
>>> print list(permutations(['1','2','3'],2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
>>>
>>> print list(permutations('abc',3))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
</pre>


## eval

The eval() expression is a very powerful built-in function of Python. It helps in evaluating an expression. The expression can be a Python statement, or a code object.
<pre>
>>> eval("9 + 5")
14
>>> x = 2
>>> eval("x + 3")
5
</pre>

Here, eval() can also be used to work with Python keywords or defined functions and variables. These would normally be stored as strings.
For example:
<pre>
>>> type(eval("len"))
type 'builtin_function_or_method'
</pre>


## Match and Extracting

- re.search() -> return True/False based on if string matches the regular expression.
- re.findall() -> if want to extract matching string

Example:
<pre>
import re
a = 'my 2 fav nos are 612 and 19'
y = re.findall('[0-9]+', a)  # [0-9]+  ==> this means one or more digits

y -> [2, 612, 19]
</pre>

**Greedy Matching**

repeat characters (* and +) push outward in both directions (greedy) to match largest possible string

example:
<pre>
import re
x = "From: using the : character"
y = re.findall('^F.+:', x)  # '^F.+:' ==> starts with F has one or more characters and ends with :
y => ['From: using the :']
</pre>
Greedy Search as it took the longest matching thing

not being greedy ==> **'^F.+?:'**  the *+?* makes it non greedy
o/p; ['From:']

Example
<pre>
text=> From: sahil@example.com sat jun  5

\S+@\S+  =>  \S means non blank character so non blank characters around @

y = re.findall('\S+@\S+', text)
y => ['sahil@example.com']

y = re.findall('^From (\S+@\S+)', text)   => (   ) => group we want to extract
y => ['sahil@example.com']

</pre>


Extract host name

text => From sahil@example.com sat jun 5

expression:

1. ===>   '\S+@(\S+)'  
2. ===>   '@([^ ]*)'  => has @ and then capture that does not have a blank character


