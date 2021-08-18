import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

MAX_VALUE = int(1e9)
N, E = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())


def dijkstra(start):
    distance = [MAX_VALUE for _ in range(N+1)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for next, next_dist in graph[now]:
            cost = dist+next_dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))
    return distance


start_to = dijkstra(1)
to_end = dijkstra(N)
v1_v2 = dijkstra(v1)[v2]

ans = min(start_to[v1]+to_end[v2]+v1_v2, start_to[v2]+to_end[v1]+v1_v2)
print(-1 if ans >= MAX_VALUE or ans < 0 else ans)
