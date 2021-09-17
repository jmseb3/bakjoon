import sys
input = sys.stdin.readline
N, M = map(int, input().split())
INF = int(1e9)

edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
distance = [INF for _ in range(N+1)]

# 벨만포드 알고리듬 사용
def bf(start):
    # 시작노드초기화
    distance[start] = 0
    # N번 반복
    for i in range(N):
        # 모든 간선에 대하여
        for j in range(M):
            now, next, cost = edges[j]
            # 현재 간선을 거쳐 이동하는게 더짧으면 갱신
            if distance[now] != INF and distance[next] > distance[now]+cost:
                distance[next] = distance[now]+cost
                # N번째에서도 값이 갱신된다면 음수 순환이 존재함
                if i == N-1:
                    return True
    return False


if bf(1):
    print(-1)
else:
    for i in range(2, N+1):
        print(-1 if distance[i] == INF else distance[i])
