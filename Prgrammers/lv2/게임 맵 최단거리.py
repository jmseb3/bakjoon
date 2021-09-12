from collections import deque

def solution(maps):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    N = len(maps)
    M = len(maps[0])
    y,x =0,0
    visited =[[False]*M for _ in range(N)]
    q = deque()
    q.append((0,0))
    while q:
        y,x = q.popleft()
        visited[y][x] = True

        for idx in range(4):
            ny = y+dy[idx]
            nx = x+dx[idx]
            if ny<0 or ny>=N or nx<0 or nx>=M:
                continue
            if not visited[ny][nx] and maps[ny][nx]!=0:
                maps[ny][nx] = maps[y][x] +1
                visited[ny][nx] = True
                q.append((ny,nx))

   
    return maps[N-1][M-1]  if visited[N-1][M-1] else -1
