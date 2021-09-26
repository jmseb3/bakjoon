INF = int(1e9)
N = int(input())

dp = [INF]*(1 << N)

graph = {}
for i in range(N):
    graph[i] = list(map(int, input().split()))

dp[0] = 0

def bit_counting(x):
    # 몇명이 작업에 투입되었는지? --> 비트에 포함된 1의 개수 세기
    answer = 0
    while x:
        answer += (x & 1)
        x >>= 1
    return answer


for i in range(1 << N):
    k = bit_counting(i)
    for j in range(N):
        if not i & (1 << j):
            dp[i | 1 << j] = min(dp[i | 1 << j], dp[i]+graph[k][j])

print(dp)
