import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
weight = [0]+list(map(int, input().split()))
graph = defaultdict(list)
dp = [[0]*2 for _ in range(N+1)]
visited = [False] * (N+1)
num = [[list(), list()] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start):
    visited[start] = True
    dp[start][0] = weight[start]
    num[start][0].append(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            dp[start][0] += dp[i][1]
            for j in num[i][1]:
                num[start][0].append(j)
            if max(dp[i][1], dp[i][0]) == dp[i][1]:
                dp[start][1] += dp[i][1]
                for k in num[i][1]:
                    num[start][1].append(k)
            else:
                dp[start][1] += dp[i][0]
                for k in num[i][0]:
                    num[start][1].append(k)


dfs(1)
if max(dp[1][0], dp[1][1]) == dp[1][0]:
    ans =dp[1][0]
    tmp =num[1][0]
else:
    ans=dp[1][1]
    tmp=num[1][1]

print(ans)
tmp.sort()
print(*tmp)
