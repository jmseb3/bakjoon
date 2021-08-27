import sys
from collections import defaultdict, deque
input = sys.stdin.readline


def bfs(node):
    q = deque([(node, None)])
    visited[node] = True
    while q:
        data = q.pop()
        for next in graph[data[0]]:
            if next != data[1] and visited[next]:
                return 0
            if next != data[1]:
                q.append((next, data[0]))
                visited[next] = True
    return 1


tc = 0
while True:
    tc += 1
    N, M = map(int, input().split())
    if [N, M] == [0, 0]:
        break
    graph = defaultdict(list)
    visited = [False] * (N+1)  # 방문 여부
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0  # 트리의 개수
    for v in range(1, N+1):
        if not visited[v]:  # 방문하지 않은 경우만 DFS 수행
            cnt += bfs(v) # 사이클이 없는 경우 트리 개수 증가
    if cnt == 0:
        print("Case {}: No trees.".format(tc))
    elif cnt == 1:
        print("Case {}: There is one tree.".format(tc))
    else:
        print("Case {}: A forest of {} trees.".format(tc, cnt))
