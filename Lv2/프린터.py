from collections import deque

def solution(priorities, location):
    answer = 0
    prioritiesDeque = deque(priorities)
    
    while True:
        priority = prioritiesDeque.popleft()
        if len(prioritiesDeque)==0 or priority>=max(prioritiesDeque):
            answer += 1
            
            if location==0:
                return answer
            else:
                location -= 1
        else:
            prioritiesDeque.append(priority)
            
            if location==0:
                location = len(prioritiesDeque) - 1
            else:
                location -= 1