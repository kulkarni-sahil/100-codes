# Enter your code here. Read input from STDIN. Print output to STDOUT

set_in_question = set(map(int, input(' ').split(' ')))
test_cases = int(input())
is_super_set = True
# print(is_super_set)
for _ in range(test_cases):
    comparison_set = set(map(int, input(' ').split(' ')))
    set_intersection = set_in_question.intersection(comparison_set)
    if len(set_intersection) != len(comparison_set) or len(set_in_question) <= len(comparison_set):
        is_super_set = False
        break
print(is_super_set)