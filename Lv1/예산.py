#https://school.programmers.co.kr/learn/courses/30/lessons/12982

from collections import deque

def solution(d, budget):
    answer = 0
    
    if sum(d) <= budget:
        return len(d)
    
    d = deque(sorted(d))
    
    while budget > 0:
        budget -= d.popleft()
        answer += 1
    
    if budget < 0:
        answer -= 1
        
    return answer