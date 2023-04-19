from collections import deque

def solution(s):
    answer = 0
    
    sDeque = deque(s)
    for i in range(len(s)):
        sDeque.rotate(-1)
        
        text = ''.join(sDeque)
        while any(s in text for s in ['()', '[]', '{}']):
            text = text.replace('()', '').replace('[]', '').replace('{}', '')
            
        if len(text)==0:
            answer += 1
        
    return answer