from collections import deque
def solution(m, n, board):
    board = [list(data) for data in board]
    answer = 0
    

    while True:
        delete = set()
        for y in range(m-1):
            for x in range(n-1):
                ck = board[y][x]
                if ck == 'X':
                    continue
                if (board[y+1][x] == ck) and (board[y][x+1] == ck) and (board[y+1][x+1] == ck):
                    delete.add((y, x))
                    delete.add((y+1, x))
                    delete.add((y, x+1))
                    delete.add((y+1, x+1))

        if not delete:
            return answer

        answer += len(delete)
        for y, x in delete:
            board[y][x] = 'X'

        for x in range(n):
            temp = deque(['X'] *m)
            for y in range(m):
                if board[y][x] !='X':
                    temp.append(board[y][x])
                    temp.popleft()
                    
            for y in range(m):
                board[y][x] = temp[y]
