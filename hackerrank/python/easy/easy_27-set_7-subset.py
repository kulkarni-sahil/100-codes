"""

You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set  is subset of set , print True.
If set  is not a subset of set , print False.

Input Format
The first line will contain the number of test cases, .
The first line of each test case contains the number of elements in set .
The second line of each test case contains the space separated elements of set .
The third line of each test case contains the number of elements in set .
The fourth line of each test case contains the space separated elements of set .

Output Format
Output True or False for each test case on separate lines.

Sample Input
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2

Sample Output
True 
False
False

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

no_of_test_cases = int(input())
for _ in range(no_of_test_cases):
    len_of_set_a = int(input())
    set_a = set(map(int, input().split(' ')))
    len_of_set_b = int(input())
    set_b = set(map(int, input().split(' ')))    
    elem_in_a_and_b = set_a.intersection(set_b)
    # print(set_a)
    # print(set_b)
    # print(elem_in_a_and_b)
    if len(elem_in_a_and_b) == len_of_set_a:
        print(True)
    else:
        print(False)
    