def solution(citations):
    answer = []
    
    if len(set(citations))==1:
        return citations[0] if len(citations) >= citations[0] else len(citations)
    
    citations = sorted(citations)
    
    for h in range(0, citations[-1]+1):
        liOver = len([j for j in citations if j >= h])  
        liLower = len([j for j in citations if j <= h]) 
        
        if h <= liOver and h >= liLower:
            answer.append(max(h, liLower))
         
    return max(answer)