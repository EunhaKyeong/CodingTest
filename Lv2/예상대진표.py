#https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    answer = 0
    
    while True:
        answer += 1

        if abs(a-b)==1 and min(a, b) % 2 == 1:
            break
            
        a = a // 2 if a % 2 == 0 else a // 2 + 1
        b = b // 2 if b % 2 == 0 else b // 2 + 1
            
    return answer