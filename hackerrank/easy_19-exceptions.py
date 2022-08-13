# Enter your code here. Read input from STDIN. Print output to STDOUT
attempts = int(input())
for _ in range(attempts):
    numerator, demoniator = (i for i in input().split(' '))    
    try:        
        _ = int(numerator)/int(demoniator)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
    


