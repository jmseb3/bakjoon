from collections import defaultdict,deque

n, m, v = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]

for i in range(1,n+1):
    graph[i] = sorted(graph[i])

dfs_visited = [False]*(n+1)
def dfs(start):
    dfs_visited[start] = True
    print(start,end=" ")
    for x in graph[start]:
        if not dfs_visited[x]:
            dfs(x)

bfs_visited = [False]*(n+1)
def bfs(start):
    queue = deque([start])
    bfs_visited[start] = True
    while queue:
        v = queue.popleft()
        print(v,end=" ")
        for x in graph[v]:
            if not bfs_visited[x]:
                queue.append(x)
                bfs_visited[x] = True


dfs(v)
print()
bfs(v)