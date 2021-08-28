import sys
from collections import defaultdict
input = sys.stdin.readline


def case(cnt, T):
    if T == 0:
        return f"Case {cnt}: No trees."
    elif T == 1:
        return f"Case {cnt}: There is one tree."
    else:
        return f"Case {cnt}: A forest of {T} trees."


def get_parent(parent, x):
    if parent[x] != x:
        parent[x] = get_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


cnt = 1
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    parent = [i for i in range(N+1)]
    graph = defaultdict(list)
    cycle_list = []
    
    for _ in range(M):
        a, b = map(int, input().split())
        if get_parent(parent, a) == get_parent(parent, b):
            cycle_list.append(a)
        else:
            union(parent, a, b)
    length = len(set(get_parent(parent, i) for i in parent))
    cycle_parent = set(get_parent(parent,x) for x in cycle_list)
    print(case(cnt, length-1-len(cycle_parent)))
    cnt += 1