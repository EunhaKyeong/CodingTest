def solution(begin, target, words):
    answer = 0
    results = [[begin for i in words]]
    
    if target not in words:
        return answer
    
    while True:
        answer += 1
        results.append([])
        
        for result in results[-2]:
            for word in words:
                if check(result, word):
                    if word==target:
                        return answer
                    else:
                        results[-1].append(word)
            
    return answer

def check(word1, word2):
    flag = False

    for idx in range(len(word1)):
        if word1[idx] != word2[idx]:
            if flag:
                return False
            else:
                flag = True
                
    return flag