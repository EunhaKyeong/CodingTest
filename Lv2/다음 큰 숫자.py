#https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):    
    cnt = str(format(n, 'b')).count('1')
    while(True):
        n += 1
        
        if cnt == str(format(n, 'b')).count('1'):
            break
        
    return n