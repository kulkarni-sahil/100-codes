"""

Task
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

Input Format
The first line contains , the number of students who have subscribed to the English newspaper.
The second line contains  space separated roll numbers of those students.
The third line contains , the number of students who have subscribed to the French newspaper.
The fourth line contains  space separated roll numbers of those students.

Output Format
Output the total number of students who have subscriptions to both English and French newspapers.

Sample Input
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output
5

"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
no_of_students_subbed_to_english_paper = int(input())
students_subbed_to_english_paper = set(map(int, input().split(' ')))

no_of_students_subbed_to_french_paper = int(input())
students_subbed_to_french_paper = set(map(int, input().split(' ')))

students_subbed_to_both_paper = students_subbed_to_english_paper.intersection(students_subbed_to_french_paper)

print(len(students_subbed_to_both_paper))