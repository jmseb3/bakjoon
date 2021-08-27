import sys
from collections import defaultdict, deque
input = sys.stdin.readline

INF = int(1e9)
N = int(input())
graph = defaultdict(list)
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    distance = [INF] * (N+1)
    distance[start] = 0
    q = deque([(0, start)])
    while q:
        dist, now = q.popleft()

        if distance[now] < dist:
            continue

        for next, cost in graph[now]:
            new = dist+cost
            if new < distance[next]:
                distance[next] = new
                q.append((new, next))
    distance[0] = 0
    return distance

tmp = dijkstra(1)
idx = tmp.index(max(tmp))

print(0 if N==1 else max(dijkstra(idx)))

