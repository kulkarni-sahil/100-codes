"""

Task
You have a non-empty set , and you have to execute  commands given in  lines.

The commands will be pop, remove and discard.

Input Format

The first line contains integer n, the number of elements in the set .
The second line contains n space separated elements of set . All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.

Output Format
Print the sum of the elements of set  on a single line.

Sample Input
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

Sample Output
4

"""

n = int(input())
s = set(map(int, input().split()))
no_of_commands = int(input())
for _ in range(no_of_commands):
    raw_cmd = input()
    if raw_cmd != 'pop':
        cmd, value = raw_cmd.split(' ')
        if cmd == 'remove':
            s.remove(int(value))
        elif cmd == 'discard':
            s.discard(int(value))
    else:
        s.pop()

print(sum(s))