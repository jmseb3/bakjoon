n = int(input())
dp = [1] *n
eletric = [list(map(int, input().split())) for _ in range(n)]

eletric.sort()

for i in range(n):
    for j in range(i):
        if eletric[i][1] > eletric[j][1]:
            dp[i]= max(dp[i],dp[j]+1)

print(n-max(dp))