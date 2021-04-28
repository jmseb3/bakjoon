
import sys


def is_sudoku(x, y, n):
    # x=행 y=열 n= 넣을값
    # 가로
    if n in board[x]:
        return False
    # 세로
    for j in range(9):
        if n == board[j][y]:
            return False
    # 사각형
    for v in range(3):
        for w in range(3):
            if n == board[(x//3)*3+v][(y//3)*3+w]:
                return False
    # 세개 만족하면 TRUE
    return True


def sudoku(x):
    if x == len(zero_board):
        for x in board:
            print(*x, sep=' ')
        exit()
    else:
        # 1~9 체크
        for i in range(1, 10):
            nx, ny = zero_board[x]

            if is_sudoku(nx, ny, i):
                board[nx][ny] = i
                sudoku(x+1)

                board[nx][ny] = 0


board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zero_board = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

sudoku(0)
