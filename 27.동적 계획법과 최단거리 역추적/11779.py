from collections import defaultdict
import heapq

N = int(input())
M = int(input())
INF = int(1e9)
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

distance = [[INF, '']]*(N+1)


def dijkstra():
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = [0, [start]]
    while q:
        dist, now = heapq.heappop(q)
        if distance[now][0] < dist:
            continue
        for next, next_cost in graph[now]:
            cost = dist + next_cost
            if cost < distance[next][0]:
                distance[next] = [cost,distance[now][1] + [next]]
                heapq.heappush(q, (cost, next))

dijkstra()
ans = distance[end]
print(ans[0])
print(len(ans[1]))
print(*ans[1])
