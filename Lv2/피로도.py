import heapq

def solution(k, dungeons):
    answer = list()
    
    find(k, dungeons, 0, answer)
    
    return -heapq.heappop(answer)

def find(k, dungeons, cnt, result):
    dungeons = list(filter(lambda x: x[0] <= k, dungeons))
    
    if len(dungeons) > 1:
        for idx in range(len(dungeons)):
            newDungeons = dungeons[0:idx] + dungeons[idx+1:]
            find(k-dungeons[idx][1], newDungeons, cnt+1, result)
    elif len(dungeons) == 1:
        heapq.heappush(result, -(cnt+1))
    else:
        heapq.heappush(result, -cnt)