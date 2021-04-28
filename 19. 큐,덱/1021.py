from collections import deque
from sys import stdin

input = stdin.readline

def moveleft(que:deque,n):
    global cnt
    for _ in range(n):
        que.append(que.popleft())
        cnt +=1

def moveright(que:deque,n):
    global cnt
    for _ in range(n):
        que.appendleft(que.pop())
        cnt +=1


n, m = map(int,input().split())
number = deque(map(int,input().split()))
que = deque(range(1,n+1,1))
cnt =0

while number:
    if number[0] == que[0]:
        que.popleft()
        number.popleft()
        m -=1
    else:
        length = len(que)
        find_index = que.index(number[0])
        if find_index <= int(length//2):
            moveleft(que,find_index)
        else:
            find_index = length - find_index
            moveright(que,find_index)

print(cnt)
