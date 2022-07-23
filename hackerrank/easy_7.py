"""

complex numbers
If we convert complex number  to its polar coordinate, we find:
r: Distance from  to origin, i.e., 
y: Counter clockwise angle measured from the positive -axis to the line segment that joins  to the origin.

Python's cmath module provides access to the mathematical functions for complex numbers.


This tool returns the phase of complex number  (also known as the argument of ).

>>> phase(complex(-1.0, 0.0))
3.1415926535897931

"""

import cmath
import math
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
cmplx = complex(a)
# print(r)
# print(type(r))
# print(r.real)
# print(r.imag)

a = cmplx.real
b = cmplx.imag

r = math.sqrt((a**2+b**2))
y = cmath.phase(cmplx)
print(r)
print(y)
