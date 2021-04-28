from collections import deque
from sys import stdin

input = stdin.readline


def push_front(que: deque, x: int):
    que.appendleft(x)

def push_back(que: deque, x: int):
    que.append(x)

def pop_front(que: deque):
    if len(que) != 0: print(que.popleft())
    else: print(-1)

def pop_back(que: deque):
    if len(que) != 0: print(que.pop())
    else: print(-1)

def size(que:deque):
    print(len(que))

def empty(que:deque):
    if que: print(0)
    else: print(1)

def front(que: deque):
    if len(que) != 0:print(que[0])
    else: print(-1)

def back(que: deque):
    if len(que) != 0:print(que[-1])
    else: print(-1)

que = deque()
for _ in range(int(input())):
    order = list(input().rstrip().split())
    
    if order[0] =='push_front' : push_front(que,order[1])
    elif order[0] =='push_back' : push_back(que,order[1])
    elif order[0] =='pop_front' : pop_front(que)
    elif order[0] =='pop_back' : pop_back(que)
    elif order[0] =='size' : size(que)
    elif order[0] =='empty' : empty(que)
    elif order[0] =='front' : front(que)
    elif order[0] =='back' :back(que)


