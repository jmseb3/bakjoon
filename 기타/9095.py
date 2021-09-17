T = int(input())

dp = [-1]*12
dp[:4] =[0,1,2,4]

for i in range(4,12):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
for _ in range(T):
    print(dp[int(input())])