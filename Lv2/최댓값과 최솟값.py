#https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    s = [int(x) for x in s.split()]
    s.sort()
    
    answer = "{} {}".format(s[0], s[-1])
    
    return answer