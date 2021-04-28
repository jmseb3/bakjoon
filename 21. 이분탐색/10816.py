import sys

input = sys.stdin.readline

n = int(input())

data_n = list(map(int, input().split()))

m = int(input())
data_m = list(map(int, input().split()))

cntdict = {}

for k in data_n:
    if k in cntdict:
        cntdict[k] +=1
    else:
        cntdict[k] = 1

for l in data_m:
    if l in cntdict:
        print(cntdict[l])
    else:
        print(0)