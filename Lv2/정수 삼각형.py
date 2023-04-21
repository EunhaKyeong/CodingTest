def solution(triangle):
    answer = triangle
    
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j==0:
                answer[i][j] += answer[i-1][j]
            elif j==i:
                answer[i][j] += answer[i-1][j-1]
            else:
                answer[i][j] += max(answer[i-1][j-1], answer[i-1][j])
        
    return max(answer[len(triangle)-1])   