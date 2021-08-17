import sys
from collections import deque, defaultdict
input = sys.stdin.readline

T = int(input())

def bfs(x):
    q = deque([x])
    visited[x] =1
    while q:
        value = q.popleft()
        for xx in graph[value]:
            if visited[xx] ==0:
                visited[xx] = -1 * visited[value]
                q.append(xx)
            elif visited[xx] == visited[value]:
                return False
    return True

for _ in range(T):
    V, E = map(int, input().split())
    visited = [0 for _ in range(V+1)]
    graph = defaultdict(list)
    possible = False
    for _ in range(E):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    for idx in range(1,V+1):
        if visited[idx] ==0:
            possible = bfs(idx)
            if not possible:
                break
    
    print("YES" if possible else "NO")