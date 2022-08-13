"""
Sample Input

7
UK
China
USA
France
New Zealand
UK
France 


Sample Output

5
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
num_of_stamps = int(input())
distinct_entries = set()
for _ in range(num_of_stamps):
    distinct_entries.add(input())

print(len(distinct_entries))