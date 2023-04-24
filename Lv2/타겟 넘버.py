def solution(numbers, target):
    answer = {}
    
    add(numbers, 0, answer)
    
    return answer[target]

def add(numbers, total, answer):
    if len(numbers) == 0:
        if total in answer:
            answer[total] += 1
        else:
            answer[total] = 1
    else:
        add(numbers[1:], total+numbers[0], answer)
        add(numbers[1:], total-numbers[0], answer)