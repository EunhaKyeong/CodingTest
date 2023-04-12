#https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0
    camera = -30000
    
    routes.sort(key=lambda x: x[1])
    
    for route in routes:
        if camera not in range(route[0], route[1]+1):
            answer += 1
            camera = route[1]
            
    return answer