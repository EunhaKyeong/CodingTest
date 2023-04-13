#https://school.programmers.co.kr/learn/courses/30/lessons/12973

from collections import deque

def solution(s):    
    if len(s) % 2 != 0:
        return 0
    
    stack = []
    for i in range(len(s)):
        if stack:
            if stack[-1]==s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
            
    if stack:
        return 0
    else:
        return 1