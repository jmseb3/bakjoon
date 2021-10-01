N, M = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]
# 일자 네모 ㄴ Z 모양은 dfs로
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# ㅗ모양은 따로 체크
shape = [
    [(0, -1), (-1, 0), (0, 1)],
    [(0, -1), (1, 0), (0, 1)],
    [(-1, 0), (1, 0), (0, 1)],
    [(-1, 0), (1, 0), (0, -1)]
]

ans = 0


def dfs(y, x, total, visited):
    global ans
    if len(visited) == 4:
        ans = max(ans, total)
        return
    for dy, dx in moves:
        ny = y + dy
        nx = x + dx
        if nx < 0 or ny < 0 or ny >= N or nx >= M:
            continue
        if (ny, nx) not in visited:
            dfs(ny, nx, total+maps[ny][nx], visited+[(ny, nx)])


def ck_shape(y, x):
    global ans
    for dir in shape:
        temp = maps[y][x]
        for dy,dx in dir:
            ny = y + dy
            nx = x + dx
            if nx < 0 or ny < 0 or ny >= N or nx >= M:
                break
            temp += maps[ny][nx]
        ans =max(ans,temp)

for y in range(N):
    for x in range(M):
        dfs(y, x, maps[y][x], [(y, x)])
        ck_shape(y,x)
print(ans)
