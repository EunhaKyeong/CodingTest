def solution(want, number, discount):
    answer = 0
    
    for idx in range(len(discount)-9):
        newDiscount = discount[idx:idx+10]
        
        flag = True
        for w, n in zip(want, number):
            if newDiscount.count(w)!=n:
                flag = False
                break
            
        if flag:
            answer += 1
            
    return answer