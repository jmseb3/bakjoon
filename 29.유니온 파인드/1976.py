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


N = int(input())
M = int(input())
parent = [i for i in range(N)]
for idx in range(N):
    data = list(map(int, input().split()))
    for ck in range(N):
        if data[ck] == 1:
            if find_parent(parent, idx) != find_parent(parent, ck):
                union(parent, idx, ck)

qry = list(map(int, input().split()))

ans = set()

for x in qry:
    ans.add(find_parent(parent,x-1))

print("YES" if len(ans) == 1 else"NO")
