def solution(n):
    answer = []
    board = [[0]*i for i in range(1,n+1)]
    x,y =-1,0
    num =1

    for i in range(n):
        for _ in range(i,n):
            if i %3 ==0:
                x +=1
            elif i%3 ==1:
                y+=1
            elif i%3==2:
                x-=1
                y-=1
            board[x][y] = num
            num +=1

    for xx in board:
        answer +=xx
    return answer