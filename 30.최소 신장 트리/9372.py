import sys
from collections import defaultdict, deque
input = sys.stdin.readline


def bfs(start):
    q = deque([start])
    visited[start] = True
    cnt = 0
    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                cnt += 1
                q.append(next)
    return cnt


INF = int(1e9)
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    visited = [False]*(N+1)
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    ans = 0
    for i in range(1, N+1):
        if not visited[i]:
            ans += bfs(i)

    print(ans)
