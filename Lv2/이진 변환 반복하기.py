#https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    cnt = 0
    total_0 = 0
    
    while(s!='1'):
        total_0 += s.count('0')
        s = format(len(s.replace('0', '')), 'b')
        cnt += 1
        
    return [cnt, total_0]