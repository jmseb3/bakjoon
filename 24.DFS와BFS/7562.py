import sys
from collections import deque
input = sys.stdin.readline

move_type = [(-1, 2), (-1, -2), (1, 2), (1, -2),
             (-2, 1), (-2, -1), (2, 1), (2, -1)]
T = int(input())


def bfs(x, y):
    visited[y][x] = True
    q = deque()
    q.append((x, y, 0))
    while q:
        x, y, cnt = q.popleft()
        if x == end_x and y == end_y:
            return cnt
        for dx, dy in move_type:
            nx = x+dx
            ny = y+dy
            if nx < 0 or nx >= L or ny < 0 or ny >= L:
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((nx, ny, cnt+1))


for _ in range(T):
    L = int(input())
    board = [[0 for _ in range(L)] for _ in range(L)]
    visited = [[False for _ in range(L)] for _ in range(L)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    print(bfs(start_x, start_y))
