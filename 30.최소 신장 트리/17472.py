from collections import deque
import sys
input = sys.stdin.readline

# 같은섬 분류하기
def bfs(start, cur):
    q = deque()
    q.append(start)
    while q:
        y, x = q.popleft()
        for idx in range(4):
            ny = y + dy[idx]
            nx = x + dx[idx]
            if ny < 0 or nx < 0 or nx >= M or ny >= N:
                continue
            if not visited[ny][nx] and arr[ny][nx]:
                visited[ny][nx] = True
                arr[ny][nx] = cur
                q.append((ny, nx))


# 다리 만들기
def bridge(maps):
    K = len(maps)
    start, cnt = 0, 0
    flag = False
    for idx in range(K):
        # 만약 값이 있고 선택된적이 없다면 시작위치설정
        if maps[idx] and not flag:
            flag = True
            start = maps[idx]
        # 값이 없고 선택된적이 있다면 거리 증가
        elif not maps[idx] and flag:
            cnt += 1
        # 값이있고 선택된 적이 있는데 그값이 다른경우(다른섬에 도착한 경우)
        elif maps[idx] and flag and start != maps[idx]:
            # 거리가 2이상이면 값을 간선에 추가
            if cnt >=2 and (start, maps[idx], cnt) not in edges:
                edges.append((start, maps[idx], cnt))
            # 값 초기화
            cnt = 0
            start = maps[idx]
        # 끝까지 도달한 경우 초기화
        elif start == maps[idx]:
            cnt = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
INF = int(1e9)
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
edges = []

idx = 1
for y in range(N):
    for x in range(M):
        if not visited[y][x] and arr[y][x]:
            arr[y][x] = idx
            bfs((y, x), idx)
            idx += 1

parent = [i for i in range(idx)]
# 가로탐색
for row in arr:
    # 도시인 경우가 있다면
    if sum(row):
        # 다리 추가 실행
        bridge(row)

# 세로 탐색
for col in list(zip(*arr)):
    if sum(col):
        bridge(col)


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges.sort(key= lambda x: x[2])
ans = 0

for start,end ,cost in edges:
    if find_parent(parent,start) != find_parent(parent,end):
        union(parent,start,end)
        ans += cost

# 모두 이어졌는지 확인
ck =len(set(map(lambda x:find_parent(parent,x), parent)))

# 2라면 ans 아니라면 -1출력
# 2인 이유는 0 이 처리 안되므로 
print(ans if ck==2 else -1)