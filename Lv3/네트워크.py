def solution(n, computers):
    answer = 0
    computerNumbers = set([number for number in range(n)])
    
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1 and i!=j:
                computers[i][j], computers[j][i] = -1, -1
                networks = findNetwork(j, computers, set([i, j]))
                answer += 1
                computerNumbers = computerNumbers - networks
    
    return answer + len(computerNumbers)

def findNetwork(i, computers, networks):
    for j in range(len(computers)):
        if computers[i][j]==1 and i!=j:
            computers[i][j], computers[j][i] = -1, -1
            networks.add(j)
            findNetwork(j, computers, networks)

    return networks