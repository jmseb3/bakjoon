n =int(input())
dp= [[1]*10 for _ in range(n)]
dp[0][0] =0

for k in range(1,n):
    dp[k][0] = dp[k-1][1]%1000000000
    for j in range(1,9):
        dp[k][j] = (dp[k-1][j-1] + dp[k-1][j+1]) %1000000000
    dp[k][9] = dp[k-1][8] %1000000000

print(sum(dp[n-1]) %1000000000)