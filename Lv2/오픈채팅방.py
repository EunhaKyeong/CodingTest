def solution(record):
    answer = []
    members = {}
    
    for r in record:
        rList = r.split(' ')
        
        if rList[0]=='Enter' or rList[0]=='Change':
            members[rList[1]] = rList[2]
        
    for r in record:
        rList = r.split(' ')
        
        if rList[0]=='Enter':
            answer.append('{}님이 들어왔습니다.'.format(members[rList[1]]))
        elif rList[0]=='Leave':
            answer.append('{}님이 나갔습니다.'.format(members[rList[1]]))
            
    return answer