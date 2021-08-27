from collections import defaultdict, deque
import sys
input = sys.stdin.readline

INF = int(1e9)
V = int(input())
edges = []
graph = defaultdict(list)
for _ in range(V):
    data = list(map(int, input().split()))
    start = data[0]
    for idx in range(1, len(data), 2):
        if data[idx] == -1:
            break
        else:
            graph[start].append((data[idx], data[idx+1]))

distance1 = [0]*(V+1)
distance2 = [0]*(V+1)


def dfs(start, distance):
    for next, dist in graph[start]:

        if distance[next] == 0:
            distance[next] = distance[start] + dist
            dfs(next, distance)


dfs(1, distance1)
distance1[1] = 0
idx = distance1.index(max(distance1))

dfs(idx, distance2)
distance2[idx] = 0
print(max(distance2))
