def trace(tc, y, x):
    if y == x:
        return []
    now = tc[y][x]
    if now is None:
        return [y, x]
    return trace(tc, y, now)[:-1]+trace(tc, now, x)

INF = int(1e9)
N = int(input())
M = int(input())
graph = [[INF]*(N+1) for _ in range(N+1)]
graph_trace = [[None]*(N+1) for _ in range(N+1)]

# 본인으로 가는 경우 초기화
for i in range(1, N+1):
    graph[i][i] = 0

# 입력받은 값 입력
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

# 알고리듬 수행 a-b /a-k-b중 짧은 거리로 갱신
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            if a == b:
                continue
            cost = graph[a][k] + graph[k][b]
            if graph[a][b] > cost:
                graph[a][b] = cost
                graph_trace[a][b] = k

for y in range(1, N+1):
    for x in range(1, N+1):
        print(0 if graph[y][x] == INF else graph[y][x], end=" ")
    print()


for y in range(1, N+1):
    for x in range(1, N+1):
        if graph[y][x] == INF:
            print(0)
            continue
        else:
            ck= trace(graph_trace, y, x)
            print(len(ck),*ck)
