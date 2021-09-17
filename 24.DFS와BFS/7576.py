import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
q = deque()
box =[]
cnt =-1
M, N = map(int, input().split())
for y in range(N):
    box.append(list(map(int,input().split())))
    for x in range(M):
        if box[y][x] == 1:
            q.append((x, y))

def bfs():
    global cnt
    while q:
        cnt +=1
        for _ in range(len(q)):
            x, y = q.popleft()
            for idx in range(4):
                nx = x+dx[idx]
                ny = y+dy[idx]
                if M > nx >= 0 and N > ny >= 0:
                    if box[ny][nx] == 0:
                        box[ny][nx] = 1
                        q.append((nx, ny))
    
bfs()
for row in box:
    if 0 in row:
        cnt =-1
        break

print(cnt)