n = int(input())
arr = list(map(int, input().split()))
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

for k in range(2, n):
    for i in range(n-k):
        if arr[i] == arr[i+k] and dp[i+1][i+k-1] == 1:
            dp[i][i+k] = 1

m = int(input())
for _ in range(m):
    start, end = map(int, input().split())
    print(dp[start-1][end-1])
