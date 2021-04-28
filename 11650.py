import sys

n = int(input())

xylist =[]
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    xylist.append([x,y])

xylist.sort()
for k in range(n):
    print(xylist[k][0],xylist[k][1])
