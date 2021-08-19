import sys
input = sys.stdin.readline
INF = int(1e9)
V, E = map(int, input().split())
graph = [[INF for _ in range(V+1)] for _ in range(V+1)]

for i in range(1, V+1):
    graph[i][i] = 0

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, V+1):
    for a in range(1, V+1):
        for b in range(1, V+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

ans = INF
for a in range(1,V+1):
    for b in range(a+1,V+1):
        if graph[a][b] != INF and graph[b][a] != INF:
            ans= min(ans,graph[a][b]+graph[b][a])

print(ans if ans!=INF else -1)
    
