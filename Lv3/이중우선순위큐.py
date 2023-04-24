from collections import deque

def solution(operations):
    answer = deque()
    
    for op in operations:
        op = op.split(' ')
        
        if op[0]=='I':
            answer.append(int(op[1]))
            continue
        
        if len(answer)!=0:
            if op[1]=='1':
                answer.remove(max(answer))
            else:
                answer.remove(min(answer))
    
    if len(answer)==0:
        return [0, 0]
    else:
        return [max(answer), min(answer)]