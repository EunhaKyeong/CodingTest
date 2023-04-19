from collections import deque

def solution(k, tangerine):
    tangerineDict = {}
    
    for t in tangerine:
        if t in tangerineDict.keys():
            tangerineDict[t] += 1
        else:
            tangerineDict[t] = 1
    
    tangerineValues = sorted(list(tangerineDict.values()), reverse=True)
    
    total = 0
    type = 0
    while total < k:
        total += tangerineValues[type]
        type += 1
    
    return type