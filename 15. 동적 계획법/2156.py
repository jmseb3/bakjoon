n = int(input())
score = [int(input()) for _ in range(n)]
dp=[0] *(n+1)

if n <=2:
    print(sum(score))
    exit
else:
    dp[1] = score[0]
    dp[2] = score[1] + score[0]

    for i in range(3,n+1):
        dp[i] = max(dp[i-2]+score[i-1],dp[i-3]+score[i-2]+score[i-1],dp[i-1])

    print(dp[n])
