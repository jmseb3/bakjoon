import sys
input = sys.stdin.readline
n, k = map(int, input().split())
good = [[0, 0]]+[list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(1, k+1):
        kg = good[i][0]
        value = good[i][1]

        if j < kg:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value+dp[i-1][j-kg], dp[i-1][j])

print(dp[n][k])