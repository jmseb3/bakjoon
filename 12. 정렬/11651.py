import sys

n = int(input())
yxlist=[]
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    yxlist.append([y,x])

yxlist.sort()


for j in range(n):
    print(yxlist[j][1],yxlist[j][0])