import sys
from collections import deque
# https://chancoding.tistory.com/38
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    que = deque(map(int,input().split()))
    cnt =0
    while que:
        top = max(que)
        m -=1
        pop = que.popleft()
        if top != pop:
            que.append(pop)
            if m < 0:
                m = len(que) -1
        else:
            cnt +=1
            if m ==-1:
                print(cnt)
                break
