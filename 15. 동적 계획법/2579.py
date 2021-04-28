n = int(input())
score = [int(input()) for _ in range(n)]
dp=[0] *n

if n <= 2:
    print(sum(score))
else:
    dp[0] = score[0]
    dp[1] = score[1] + dp[0]
    dp[2] = score[2] + max(score[1],score[0])

    for k in range(3,n):
        dp[k] = score[k] +max(score[k-1]+dp[k-3] ,dp[k-2])

    print(dp[-1])