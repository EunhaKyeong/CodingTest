#https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):    
    #방문한 길
    roads = deque([(0, 0)])    
    
    #최단 경우를 구하는 맵
    visited = [[0 for j in range(len(maps[i]))] for i in range(len(maps))]  
    visited[0][0] = 1
    
    #상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while roads:
        x, y = roads.popleft()
        
        if x==len(maps)-1 and y==len(maps[0])-1:
            break
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if visited[nx][ny]==0 and maps[nx][ny]==1:
                    visited[nx][ny] = visited[x][y] + 1
                    roads.append((nx, ny))
    
    if visited[-1][-1] == 0:
        return -1
    else:
        return visited[-1][-1]