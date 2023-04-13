#https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0
    lastNum = int(n / 2)
    
    for i in range(1, lastNum+1):
        num = i
        
        while(True):
            i += 1
            num += i
            
            if num == n:
                answer += 1
                break
            elif num > n:
                break
                
    return answer + 1