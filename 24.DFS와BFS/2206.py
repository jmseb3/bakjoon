import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
q.append([0, 0, 1])

visited[0][0][1] = 1


def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    while q:
        x, y, status = q.popleft()
        if x == M-1 and y == N-1:
            return visited[y][x][status]
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if not (nx < 0 or nx >= M or ny < 0 or ny >= N):
                if arr[ny][nx] == 1 and status == 0:
                   visited[ny][nx][1] = visited[y][x][0] + 1
                   q.append((nx, ny, 1))
                elif arr[ny][nx] ==0 and visited[ny][nx][status] ==0:
                    visited[ny][nx][status] = visited[y][x][status] + 1
                    q.append((nx,ny,status))
    return -1
print(bfs())