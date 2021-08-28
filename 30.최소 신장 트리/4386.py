import sys
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


def get_dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5


N = int(input())

data = [list(map(float, input().split())) for _ in range(N)]
parent = [i for i in range(N+1)]
edges = []
for i in range(N):
    for j in range(i+1, N):
        a = data[i]
        b = data[j]
        dist = get_dist(a, b)
        edges.append((a, b, dist))

edges.sort(key=lambda x: x[2])
ans = 0
for a, b, cost in edges:
    if find_parent(parent, data.index(a)) != find_parent(parent, data.index(b)):
        union(parent, data.index(a), data.index(b))
        ans += cost

print(ans)
