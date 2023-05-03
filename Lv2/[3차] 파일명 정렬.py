import re

def solution(files):
    answer = []
    filesDict = {}
    
    for file in files:
        number = re.findall(r'\d+', file)[0]
        head = file.split(number)[0].upper()
        number = number.lstrip('0')
        
        if len(number)==0:  #숫자가 0이면 다 지워질 수도 있다.
            number = 0
        else:
            number = int(number)
        
        if head not in filesDict:
            filesDict[head] = {}
            
        if number not in filesDict[head]:
            filesDict[head][number] = []
            
        filesDict[head][number].append(file)
    
    headSorted = sorted(filesDict)
    for head in headSorted:
        numberSorted = sorted(filesDict[head])
        
        for number in numberSorted:
            answer += filesDict[head][number]
    
    return answer