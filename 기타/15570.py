import sys
sys.setrecursionlimit(10**6)


N, M = map(int, input().split())
MOD = 1999


def fast_pow(base, power):
    result = 1
    while power > 0:
        # If power is odd
        if power % 2 == 1:
            result = (result * base)
        power = power // 2
        base = (base * base)
    return result % MOD


def solution(N, M):
    if N > M:
        return fast_pow(2, M-1) % MOD

    dp = [0]*(M+1)
    dp[1] = 1
    for idx in range(2, N):
        dp[idx] = (2*dp[idx-1] % MOD
    for idx in range(N, M+1):
        if idx%N==0:
            dp[idx] =
       dp[idx] = (dp[idx-1][0]*2 % MOD, dp[idx-1][1]+1 % MOD)
    print(dp)
    return dp[M]


print(solution(N, M))
