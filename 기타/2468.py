from collections import deque

N = int(input())
maps = []
max_len = 0
for _ in range(N):
    temp = list(map(int, input().split()))
    max_len = max(max_len, max(temp))
    maps.append(temp)
moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
ans = 0


def bfs(y, x, ck, visited):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    while q:
        y, x = q.popleft()
        for dy, dx in moves:
            ny = y + dy
            nx = x + dx
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            if maps[ny][nx] >= ck and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))


for ck in range(max_len+1):
    tmp = 0
    visited = [[False]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if maps[y][x] >= ck and not visited[y][x]:
                bfs(y, x, ck, visited)
                tmp += 1
    ans = max(tmp, ans)

print(ans)
