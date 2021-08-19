from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

case = int(input())
INF = int(1e9)


def dijkstra(start):
    distance = [INF for _ in range(N+1)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next, next_dist in graph[now]:
            cost = dist + next_dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))
    return distance


for _ in range(case):
    N, M, T = map(int, input().split())
    S, G, H = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    ds, dg, dh = dijkstra(S), dijkstra(G), dijkstra(H)
    ans = []
    for _ in range(T):
        end = int(input())
        if (ds[G]+dg[H]+dh[end] == ds[end]) or (ds[H]+dh[G]+dg[end] == ds[end]):
            ans.append(end)
    ans.sort()
    print(*ans)
