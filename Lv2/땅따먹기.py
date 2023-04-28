def solution(land):    
    result = [[0 for j in range(len(land[0]))] for i in range(len(land))]
    
    for i in range(len(result)):
        for j in range(len(result[0])):
            if i == 0:
                result[i][j] = land[i][j]
            else:
                result[i][j] = land[i][j] + max(result[i-1][:j] + result[i-1][j+1:])
                
    return max(result[-1])