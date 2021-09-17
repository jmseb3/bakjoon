import sys,heapq
from collections import defaultdict

input = sys.stdin.readline

V,E = map(int,input().split())
start = int(input())
graph = defaultdict(list)
MAX_VALUE = int(1e9)
distance = [MAX_VALUE for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

def dijkstra():
    q =[]
    heapq.heappush(q,(0,start))
    distance[start] =0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for next, next_cost in graph[now]:
            cost = dist + next_cost
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q,(cost,next))
dijkstra()

for idx in range(1,V+1):
    print(distance[idx] if distance[idx]!=MAX_VALUE else "INF")