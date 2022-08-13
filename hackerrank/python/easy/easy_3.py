if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    x = sorted(arr, reverse=True)
    winner_score = x[0]
    for score in x[1:]:
        if score != winner_score:
            print(score)
            break