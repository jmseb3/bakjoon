
def solution(dirs):
    move = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0),
    }
    answer = 0
    visited = set()
    x, y = 0, 0

    for oper in dirs:
        dx, dy = move[oper]
        nx, ny = x+dx, y+dy
        if nx>5 or nx<-5 or ny>5 or ny<-5:
            continue
        go = (x, y, nx, ny)
        back = (nx, ny, x, y)
        x,y = nx,ny
        if go not in visited:
            visited.add(go)
            visited.add(back)


    return len(visited)//2
