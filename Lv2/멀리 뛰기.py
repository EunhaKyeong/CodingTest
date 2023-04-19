import math

def solution(n):
    answer = 0
    
    for i in range(n // 2 + 1):
        one = n - 2 * i
        answer += math.factorial(one + i) // (math.factorial(one) * math.factorial(i))
        
    return answer % 1234567