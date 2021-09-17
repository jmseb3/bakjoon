from collections import deque

N, K = map(int, input().split())

MAX_NUM = 100_001
move = [-1]*MAX_NUM
path = []


def possible(a):
    if 0 <= a < MAX_NUM:
        return True
    return False


def bfs(start):
    q = deque([(start, 0)])
    while q:
        now, time = q.popleft()
        if now == K:
            tmp = now
            while tmp != start:
                path.append(tmp)
                tmp = move[tmp]
            path.append(start)
            return time

        next = [now-1, now+1, now*2]
        for x in next:
            if possible(x) and move[x] == -1:
                move[x] = now
                q.append((x, time+1))


print(bfs(N))
print(*path[::-1])
