import sys
from collections import deque
input = sys.stdin.readline
def push(que,x):
    que.append(x)

def pop (que):
    if (len(que) ==0) : return -1
    temp = que[0]
    que.popleft()
    return temp

def size(que):
    return len(que)

def empty(que):
    if (len(que) ==0) : return 1
    else: return 0

def front(que):
    if (len(que) ==0) : return -1
    return que[0]

def back(que):
    if (len(que) ==0) : return -1
    return que[-1]

que = deque([])

for i in range(int(input())):
    order = input().rstrip().split()
    if (order[0]=='pop') : print(pop(que))
    elif (order[0]=='size') : print(size(que))
    elif (order[0]=='empty') : print(empty(que))
    elif (order[0]=='front') : print(front(que))
    elif (order[0]=='back') : print(back(que))
    else: push(que,int(order[1]))
