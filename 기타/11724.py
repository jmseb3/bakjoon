N, M = map(int, input().split())

parent = [i for i in range(N+1)]


def find_parent(parent, a):
    if parent[a] != a:
        return find_parent(parent, parent[a])
    return parent[a]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(M):
    u, v = map(int, input().split())
    union_parent(parent,u,v)

ans = set()
for ck in parent[1:]:
    ans.add(find_parent(parent,ck))
    
print(len(ans))
