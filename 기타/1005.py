from collections import defaultdict, deque


def topology_sort(target):
    dp = [0]*(N+1)

    q = deque()
    for i in range(1,N+1):
        if in_degree[i] ==0:
            q.append(i)
            dp[i] += data[i]
    
    while q:
        now =q.popleft()

        for i in graph[now]:
            in_degree[i] -=1
            dp[i] = max(dp[i],dp[now]+data[i])

            if in_degree[i] ==0:
                q.append(i)
    return dp[target]


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    data = [0]+list(map(int, input().split()))
    graph = defaultdict(list)
    in_degree = [0] * (N+1)

    for _ in range(K):
        start, end = map(int, input().split())
        graph[start].append(end)
        in_degree[end] += 1

    print(topology_sort(int(input())))
