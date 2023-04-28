def solution(dirs):
    answer = 0
    position = [0, 0]
    roads = list()
    
    for dir in list(dirs):
        if dir=='U' and position[1] < 5:
            position = [position[0], position[1] + 1]
        elif dir=='D' and position[1] > -5:
            position = [position[0], position[1] - 1]
        elif dir=='R' and position[0] < 5:
            position = [position[0] + 1, position[1]]
        elif dir=='L' and position[0] > -5:
            position = [position[0] - 1, position[1]]
        else:
            continue
        
        road = []
        if len(roads)==0:
            road = [[0, 0], position]
        else:
            road = [roads[-1][-1], position]        
        roads.append(road)

        if roads.count(road) + roads.count(road[::-1])==1:
            answer += 1
            
    return answer