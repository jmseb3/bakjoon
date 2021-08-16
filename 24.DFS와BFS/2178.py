import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited[0][0] = 1

def bfs():
    q = deque([[0, 0]])
    while q:
        x, y = q.popleft()
        if y == n-1 and x == m-1:
            return visited[y][x]

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if visited[ny][nx] == 0 and arr[ny][nx] == 1:
                visited[ny][nx] = visited[y][x] + 1
                q.append([nx, ny])
bfs()
print(visited[n-1][m-1])
