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
