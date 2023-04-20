import math

def solution(clothes):    
    clothesDict = {}
    for cloth in clothes:
        if cloth[1] in clothesDict.keys():
            clothesDict[cloth[1]].append(cloth[0])
        else:
            clothesDict[cloth[1]] = [cloth[0]]
            
    top = 1
    bottom = 1
    for cloth in clothesDict.values():
        top *= math.factorial(len(cloth) + 1)
        bottom *= math.factorial(len(cloth))

    return top / bottom - 1