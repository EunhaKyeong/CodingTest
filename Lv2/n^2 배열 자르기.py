def solution(n, left, right):
    answer = []
    
    for idx in range(left, right+1):
        (row, col) = idx // n, idx % n
                
        if row < col:
            answer.append(col+1)
        else:
            answer.append(row+1)
    
    return answer