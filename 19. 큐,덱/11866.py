import sys

input = sys.stdin.readline
n, k = map(int,input().split())

que = list(range(1,n+1))
result =[]

snum =0
while True:
    cnt = 1
    while cnt != k:
        cnt +=1
        que.append(que.pop(0))
    result.append(que.pop(0))
    snum +=1
    if snum == n:
        break

print("<",end="")
print(*result,sep=", ",end="")
print(">")
