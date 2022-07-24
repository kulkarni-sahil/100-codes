"""

input:
1 4
x**3 + x**2 + x + 1

ouput:
True

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
x, y = (int(r) for r in input().split())
eq = input()
# print(eq)
replacesd_eq = eq.replace('x', str(x))
# print(replacesd_eq)
q = eval(replacesd_eq)
# print(q)
# print(type(q))

print(q==y)
