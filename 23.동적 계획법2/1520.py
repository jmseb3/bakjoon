import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dp[n-1][m-1] =1
def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    res = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0>nx or 0>ny or nx>=n or ny>=m:
            continue
        if arr[nx][ny] <arr[x][y]:
            res += dfs(nx,ny)
    dp[x][y] = res
    return res

dfs(0,0)
print(dp[0][0])