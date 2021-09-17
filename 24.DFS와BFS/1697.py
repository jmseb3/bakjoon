from collections import deque

n, k = map(int, input().split())
max_ = 100001
arr = [0] * max_


def bfs():
    queue = deque([n])
    while queue:
        v = queue.popleft()
        if v == k:
            return arr[v]
        for x in [v-1, v+1, 2*v]:
            if(x >= 0 and x < max_ and not arr[x]):
                arr[x] = arr[v]+1
                queue.append(x)


print(bfs())