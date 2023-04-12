#https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = " ".join(map(jadenCase, s.split(" ")))

    return answer

def jadenCase(word):    
    if word=="":
        return word
    else:
        return word[0].upper() + word[1:].lower()