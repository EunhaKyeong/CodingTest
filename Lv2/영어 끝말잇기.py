#https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    for i in range(len(words)):
        if words[0:i].count(words[i])!=0:
            first = getFirst(i, n)
            second = (i+1 + (n-first)) / n
            return [first, second]
            
        if i!=0 and words[i-1][-1]!=words[i][0]:
            first = getFirst(i, n)
            second = (i+1 + (n-first)) / n
            return [first, second]

    return [0, 0]

def getFirst(idx, n):
    result = (idx+1) % n
    
    if result == 0:
        return n
    else:
        return result