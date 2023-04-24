def solution(n, s):
    if n > s:
        return [-1]
        
    answer = []
    quotient = s // n
    remainder = s % n
    
    for i in range(n):
        if i < remainder:
            answer.append(quotient + 1)
        else:
            answer.append(quotient)
        
    return sorted(answer)