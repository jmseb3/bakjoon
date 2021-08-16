import sys
input = sys.stdin.readline

n, m = map(int, input().split())

bytes = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
sum_c = sum(costs)
dp = [[0 for _ in range(sum_c+1)] for _ in range(n+1)]

ans = sum_c

for i in range(1, n+1):
    byte = bytes[i]
    cost = costs[i]

    for j in range(1,sum_c+1):
        if j <cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(byte+dp[i-1][j-cost],dp[i-1][j])

        if dp[i][j] >=m:
            ans = min(ans,j)

if m !=0: print(ans)
else: print(0)