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


V, E = map(int, input().split())
parent = [i for i in range(V+1)]
edges =[list(map(int,input().split())) for _ in range(E)]
edges.sort(key=lambda x:x[2])

ans =0
for a,b,c in edges:
    if find_parent(parent,a) != find_parent(parent,b):
        union(parent,a,b)
        ans +=c
print(ans)
    
