from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
if n ==1:
    print(1)
    exit()
    
que = deque(list(range(n,0,-1)))
while True:
    que.pop()
    if len(que) ==1:
        break

    temp = que[-1]
    que.pop()
    que.appendleft(temp)
print(que[0])