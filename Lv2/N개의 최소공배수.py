def solution(arr):    
    maxValue = max(arr)
    i = 1
    
    while True:        
        result = [a for a in arr if maxValue * i % a != 0]
        
        if len(result)==0:
            return maxValue * i
        else:
            i += 1    