import sys
from collections import deque
input = sys.stdin.readline

move_type = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
q = deque()
cnt = -1
M, N, H = map(int, input().split())
total = []
for z in range(H):
    box = []
    for y in range(N):
        box.append(list(map(int, input().split())))
        for x in range(M):
            if box[y][x] == 1:
                q.append((x, y, z))
    total.append(box)

def bfs():
    global cnt
    while q:
        cnt += 1
        for _ in range(len(q)):
            x, y, z = q.popleft()
            for dx, dy, dz in move_type:
                nx, ny, nz = x+dx, y+dy, z+dz
                if M > nx >= 0 and N > ny >= 0 and H > nz >= 0:
                    if total[nz][ny][nx] == 0:
                        total[nz][ny][nx] =1
                        q.append((nx, ny, nz))

bfs()
for box in total:
    for row in box:
        if 0 in row:
            cnt =-1
            break
print(cnt)
