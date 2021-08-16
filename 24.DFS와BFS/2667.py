import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
# 우 하 좌 상
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False for _ in range(n)] for _ in range(n)]


def dfs(x, y):
    res = 1
    visited[y][x] = True
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if visited[ny][nx] or arr[ny][nx] == 0:
            continue
        visited[ny][nx] = True
        res += dfs(nx, ny)
    return res


ans = []
for y in range(n):
    for x in range(n):
        if arr[y][x] == 1 and not visited[y][x]:
            ans.append(dfs(x, y))

print(len(ans))
ans.sort()
for x in ans: print(x)
