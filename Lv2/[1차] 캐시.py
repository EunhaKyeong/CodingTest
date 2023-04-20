from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    
    for city in cities:
        city = city.upper()
        
        if city in cache:            
            cache.remove(city)
            cache.appendleft(city)
            
            answer += 1
        else:
            cache.appendleft(city)
            answer += 5
                
        
    return answer