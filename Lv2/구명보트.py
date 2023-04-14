#https://school.programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque

def solution(people, limit):
    answer = 0
    
    people.sort()
    peopleDeque = deque(people)
    
    while len(peopleDeque) > 1:
        light = peopleDeque.popleft()
        
        if light + peopleDeque.pop() > limit:
            peopleDeque.appendleft(light)
        
        answer += 1
        
    return answer + len(peopleDeque)