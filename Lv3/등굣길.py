def solution(m, n, puddles):    #m: 열, n: 행
    maps = [[1 for col in range(m)] for row in range(n)]

    for row in range(n):
        for col in range(m):
            
            if [col+1, row+1] in puddles:
                maps[row][col] = 0
                continue
                
            if row==0 and col==0:
                continue
                
            if row==0:
                maps[row][col] = maps[row][col-1]
                continue
                
            if col==0:
                maps[row][col] = maps[row-1][col]
                continue
                
            maps[row][col] = maps[row-1][col] + maps[row][col-1]
                
    return maps[n-1][m-1] % 1000000007