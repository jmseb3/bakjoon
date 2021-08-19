import sys
input = sys.stdin.readline

INF = int(1e9)
N = int(input())
M = int(input())
graph = [[INF]*(N+1) for _ in range(N+1)]

# 플로이드 와셜 알고리듬
# graph[a][b] : a에서 b로가는 비용

# 본인으로 가는 경우 초기화
for i in range(1, N+1):
    graph[i][i] = 0

# 입력받은 값 입력 (중복이 있을수 있으므로 체크)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

# 알고리듬 수행 a-b /a-k-b중 짧은 거리로 갱신
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for row in graph[1:]:
    for idx in range(1, N+1):
        if row[idx] == INF:
            print(0, end=" ")
        else:
            print(row[idx], end=" ")
    print()
