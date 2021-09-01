n = int(input())


def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 1
    for idx in range(3,n+1):
        dp[idx] = dp[idx-2] + dp[idx-1]
    return dp[n]

print(solution(n))