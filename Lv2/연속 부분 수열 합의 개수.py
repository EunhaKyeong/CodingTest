from collections import deque

def solution(elements):
    answer = set()
    elementsDeque = deque(elements)
    
    for i in range(len(elementsDeque)):
        sum = 0
        elementsDeque.rotate(-1)
        
        for j in range(len(elementsDeque)):
            sum += elementsDeque[j]
            answer.add(sum)
    
    return len(answer)