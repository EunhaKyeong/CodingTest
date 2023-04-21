from collections import deque

def solution(str1, str2):    
    str1Deque = deque()
    for i in range(len(str1) - 1):
        element1 = str1[i:i+2]
        
        if element1.isalpha():
            str1Deque.append(element1.upper())
            
    str2Deque = deque()
    for i in range(len(str2) - 1):
        element2 = str2[i:i+2]
        
        if element2.isalpha():
            str2Deque.append(element2.upper())
    
    intersectionDeque = deque()
    unionDeque = deque()
    while len(str1Deque)!=0 and len(str2Deque)!=0:
        deque1 = str1Deque.pop()
        
        if str2Deque.count(deque1) > 0:
            intersectionDeque.append(deque1)
            str2Deque.remove(deque1)
        else:
            unionDeque.append(deque1)
    unionDeque += intersectionDeque + str1Deque + str2Deque
                       
    if len(intersectionDeque)==0 and len(unionDeque)==0:
        return 65536
    else:
        return int(len(intersectionDeque) / len(unionDeque) * 65536)