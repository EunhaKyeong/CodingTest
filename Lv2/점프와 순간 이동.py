#https://school.programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    ans = 0
    
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = int(n // 2)
            ans += 1
    
    return ans+1