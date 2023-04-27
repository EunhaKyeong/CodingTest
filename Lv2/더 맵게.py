import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    while len(scoville) >= 2:
        newK = heapq.heappop(scoville)
        
        if newK >= K:
            return answer
        else:
            newK += heapq.heappop(scoville) * 2
            heapq.heappush(scoville, newK)
            answer += 1
            
    if len(scoville)==1 and heapq.heappop(scoville)>=K:
        return answer
    else:
        return -1