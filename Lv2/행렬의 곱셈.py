def solution(arr1, arr2):
    answer = [[0 for j in range(len(arr2[0]))] for i in range(len(arr1))]

    for i in range(len(answer)):
        for j in range(len(answer[i])):
            answer[i][j] = multiply(i, j, arr1, arr2)
        
    return answer

def multiply(i, j, arr1, arr2):
    result = 0
    
    for idx in range(len(arr1[i])):
        result += (arr1[i][idx] * arr2[idx][j])
        
    return result