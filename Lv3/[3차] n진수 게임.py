def solution(n, t, m, p):
    num = 0 # n진법으로 변환할 숫자
    notation = ['0']    # n진법으로 변환된 숫자
    order = 1   # 진행된 게임 횟수
    answer = '' # 정답
    
    if m == p:  # 세명의 게임에서 세번째 순서면 나머지(order % m)가 0이 돼야 함.
        p = 0
        
    while len(answer) < t:
        if len(notation) == 0:
            num += 1
            notation = list(convert_notation(num, n))
            
        firstNum = notation.pop(0)
        
        if order % m == p:
            answer += firstNum
            
        order += 1
        
    return answer

def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert_notation(q, base) + T[r] if q else T[r]