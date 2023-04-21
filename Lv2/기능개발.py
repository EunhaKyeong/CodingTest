from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque()
    
    for progress, speed in zip(progresses, speeds):
        remain = 100 - progress
        release = remain // speed if remain % speed == 0 else (remain // speed) + 1
        
        if len(days)==0:
            days.append(release)
        else:
            if max(days) >= release:
                days.append(release)
            else:
                answer.append(len(days))
                days.clear()
                days.append(release)   
                
    answer.append(len(days))
    
    return answer