# Regex and Python

https://xkcd.com/208/

## Quick Guide

<pre>
^ : Matches start of line
$ : Matched end of line
. : any character
\s : matches white space
\S : matches any Non White Space character
* : repeats a character zero or more times
*? : repeats a character zero or more times (non-greedy)
+ : repeats a character one or more times
+? : repeats a character one or more times (non-greedy)
[aeiou] : Matches a single character in the listed set
[^XYZ] : Matches a single character NOT listed in the set
[a-z0-9] : set of characters can include a range
( : indicates where string extraction is to start
) : indicates where string extraction has to end
</pre>


- import re
- re.search() to see if a string matches a regular expression, similar to find() method of strings
- re.findall() extract portions of a string that matches your regular expression, similar to *find()* and slicing: var[5:10]

## search vs find

<pre>

options 1:

if line.find('From: ') > 0:
    pass

options 2:

import re
if re.search('From: ', line):
    pass

</pre>

- line startswith From:
<pre>

options 1:

if line.startswith('From: ') > 0:
    pass

options 2:

import re
if re.search('^From: ', line):  # "^From: "
    pass

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
