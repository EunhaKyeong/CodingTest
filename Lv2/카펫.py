#https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):    
    bWidth = 3
    
    while True:
        yWidth = bWidth - 2
        
        if yellow % yWidth == 0:
            yHeight = yellow / yWidth
            
            if bWidth * 2 + yHeight * 2 == brown and bWidth >= yHeight+2:
                return [bWidth, yHeight+2]
            
        bWidth += 1