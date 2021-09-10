def solution(board):
    N = len(board)
    M = len(board[0])
    for y in range(1,N):
        for x in range(1,M):
            if board[y][x] ==1:
                board[y][x] = min(board[y-1][x-1],min(board[y-1][x],board[y][x-1]))+1
    for xx in board:
        print(xx)
    return max([item for row in board for item in row])**2