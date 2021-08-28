import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


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


N, M = map(int, input().split())
parent = [i for i in range(N)]
cycle = False
ck = False
ans = 0
for i in range(M):
    a, b = map(int, input().split())
    if cycle:
        continue
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        ans = i+1
    else:
        union(parent, a, b)

print(ans)
