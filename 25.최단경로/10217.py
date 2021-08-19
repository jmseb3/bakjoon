from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = deque()
    q.append((0, start, 0))
    distance[start][0] = 0
    while q:
        dist, now, cost = q.popleft()
        if distance[now][cost] < dist:
            continue
        for next, next_cost, next_dist in graph[now]:
            ref_dist = dist + next_dist
            ref_cost = cost + next_cost
            if ref_cost > M:
                continue
            if ref_dist < distance[next][ref_cost]:
                distance[next][ref_cost] = ref_dist
                q.append((ref_dist, next, ref_cost))


T = int(input())
INF = int(1e9)
for _ in range(T):
    graph = defaultdict(list)
    N, M, K = map(int, input().split())
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))
    # 시간 비용
    distance = [[INF for _ in range(M+1)] for _ in range(N+1)]
    dijkstra(1)
    ans = min(distance[N])
    print(ans if ans != INF else "Poor KCM")
