"""

i/p
10                                     
161 182 161 154 176 170 167 171 170 174 

o/p
avg of distinct hts

"""

def average(array):
    # your code goes here
    distinct_ht = set(array)
    return (sum(distinct_ht)/len(distinct_ht))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)