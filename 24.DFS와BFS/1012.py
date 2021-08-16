import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

t = int(input())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x, y):
    if(bachu[y][x]==1):
        bachu[y][x] =0
        for idx in range(4):
            nx = x+dx[idx]
            ny = y+dy[idx]
            if (nx<0 or nx>=m or ny<0 or ny>=n):
                continue
            dfs(nx,ny)



for _ in range(t):
    m, n, k = map(int, input().split())
    bachu = [[0] * m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        bachu[y][x] = 1
    
    for y in range(n):
        for x in range(m):
            if(bachu[y][x]==1):
                cnt+=1
                dfs(x,y)
    print(cnt)