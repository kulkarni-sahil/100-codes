"""
This function returns a list of tuples. The th tuple contains the th element from each of the argument sequences or iterables.

If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence.


>>> print zip([1,2,3,4,5,6],'Hacker')
[(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
>>> 
>>> print zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
[(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]
>>> 
>>> A = [1,2,3]
>>> B = [6,5,4]
>>> C = [7,8,9]
>>> X = [A] + [B] + [C] => [[1,2,3], [6,5,4], [7,8,9]]
>>> 
>>> print zip(*X)
[(1, 6, 7), (2, 5, 8), (3, 4, 9)]

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
studs, subjs = (int(i) for i in input().split(' '))
# print(studs)
# print(subjs)

marks = []
for _ in range(subjs):
    raw_iput_str = input()
    # print(raw_iput_str)
    marks.append([float(i) for i in raw_iput_str.split(' ')])

for each_stud_marks in zip(*marks):
    avgg = sum(each_stud_marks)/len(each_stud_marks)
    print("{:.1f}".format(avgg))
