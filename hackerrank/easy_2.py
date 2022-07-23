if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    import itertools
    x_list = [i for i in range(x+1)]
    y_list = [i for i in range(y+1)]
    z_list = [i for i in range(z+1)]
        
    op = []
    for i, j, k in itertools.product(x_list, y_list, z_list):
        # print(i,j,k)
        if i+j+k != n:
            op.append([i,j,k])
            
    print(op)