import sys
from collections import deque
input = sys.stdin.readline

st1 = list(input().rstrip())
st2 = deque()
M = int(input())
for _ in range(M):
    qrys = list(map(str, input().split()))
    if qrys[0] == "L":
        if st1:
            st2.appendleft(st1.pop())
    elif qrys[0] == "D":
        if st2:
            st1.append(st2.popleft())
    elif qrys[0] == "B":
        if st1:
            st1.pop()
    else:
        st1.append(qrys[1])

print(''.join(st1 + list(st2)))