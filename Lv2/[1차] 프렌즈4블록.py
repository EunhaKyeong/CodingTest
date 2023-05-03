def solution(m, n, board):
    answer = 0
    
    for i in range(len(board)):
        board[i] = list(board[i])
        
    while True:
        blocks = set()
                
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == '':
                    continue
                
                if board[i][j]==board[i][j+1] and board[i][j]==board[i+1][j] and board[i][j]==board[i+1][j+1]:
                    blocks.add((i, j))
                    blocks.add((i+1, j))
                    blocks.add((i, j+1))
                    blocks.add((i+1, j+1))
                                      
        if len(blocks)==0:
            break
        else:
            answer += len(blocks)
                                
        for block in blocks:
            board[block[0]][block[1]] = ''
                        
        while True:
            moved = False
            
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j]=='':
                        board[i+1][j] = board[i][j]
                        board[i][j] = ''
                        moved = True
                        
            if not moved:
                break
                        
    return answer