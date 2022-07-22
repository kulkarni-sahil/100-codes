if __name__ == '__main__':
    student_info = list()
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append(score)
        student_info.append([name, score])
        
    scores_sorted = sorted(score_list)
    second_lowest_score = scores_sorted[1]
    
    studs = sorted([stud_info[0] for stud_info in student_info if stud_info[1] == second_lowest_score])
    
    for i in studs:
        print(i)
    