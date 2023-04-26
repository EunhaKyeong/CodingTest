import heapq

def solution(n, works):
    if sum(works) > n:
        workHeap = []
        
        for work in works:
            heapq.heappush(workHeap, -work)
        
        while n > 0:
            heapq.heappush(workHeap, heapq.heappop(workHeap) + 1)
            n -= 1
    else:
        return 0
            
    answer = 0
    for work in workHeap:
        answer += (-work)**2
            
    return answer