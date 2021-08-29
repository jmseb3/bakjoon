import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, R, Q = map(int, input().split())

edges = defaultdict(list)
subtree = [0]*(N+1)
visited = [False]*(N+1)
for _ in range(N-1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)


def dfs(root):
    subtree[root] = 1
    visited[root] = True
    for i in edges[root]:
        if not visited[i]:
            dfs(i)
            subtree[root] += subtree[i]
    return
    
dfs(R)
for _ in range(Q):
    qry = int(input())
    print(subtree[qry])
