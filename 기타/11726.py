n = int(input())

MOD =10_007

def solution(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for idx in range(3,n+1):
        dp[idx] = (dp[idx-1] + dp[idx-2])%MOD
    
    return dp[n]
print(solution(n))