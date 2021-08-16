from collections import defaultdict,deque
n = int(input())
m = int(input())

graph = defaultdict(list)

for _ in range(m):
    x,y = map(int,input().split())
    graph[x] +=[y]
    graph[y] +=[x]

for i in range(1,n+1):
    graph[i] = sorted(graph[i])

visted=[False]*(n+1)
ans =0
# def dfs(start):
#     global ans
#     visted[start] = True
#     for x in graph[start]:
#         if not visted[x]:
#             ans +=1
#             dfs(x)

def bfs(start):
    global ans
    queue = deque([start])
    while queue:
        v = queue.popleft()
        visted[v] = True
        for x in graph[v]:
            if not visted[x]:
                queue.append(x)
                ans +=1
                visted[x] = True

# dfs(1)
bfs(1)
print(ans)