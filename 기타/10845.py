from collections import deque
import sys
input = sys.stdin.readline

q = deque()

N = int(input())

for _ in range(N):
    qrys = list(map(str, input().rstrip().split()))
    qry = qrys[0]
    if qry == "push":
        q.append(int(qrys[1]))
    elif qry == "pop":
        print(q.popleft() if q else -1)
    elif qry == "size":
        print(len(q))
    elif qry == "empty":
        print(0 if q else 1)
    elif qry == "front":
        print(q[0] if q else -1)
    elif qry == "back":
        print(q[-1] if q else -1)
