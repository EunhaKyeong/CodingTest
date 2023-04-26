import math 

def solution(n, k):
    answer = 0
    num = ''
    
    while n > 0:
        n, mod = divmod(n, k)
        num += str(mod)
        
    num = num[::-1]
    primes = num.split('0')

    for prime in primes:
        if prime not in ['', '1'] and primenumber(int(prime)):
            answer += 1
    
    return answer

# 소수 판별
def primenumber(x):
    for i in range (2, int(math.sqrt(x) + 1)):	# 2부터 x의 제곱근까지의 숫자
    	if x % i == 0:		# 나눠떨어지는 숫자가 있으면 소수가 아님
        	return False
        
    return True				# 전부 나눠떨어지지 않는다면 소수임