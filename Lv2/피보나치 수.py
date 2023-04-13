#https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    answer = 0
    
    nums = [0, 1]
    for i in range(2, n+1):
        nums.append(nums[i-2] + nums[i-1])
        
    return nums[n] % 1234567