import sys

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
matrixA=[list(map(int,input().rstrip().split())) for _ in range(n)]

m,k = map(int,input().rstrip().split())
matrixB=[list(map(int,input().rstrip().split())) for _ in range(m)]

matrixans=[[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for t in range(m):
            matrixans[i][j] += matrixA[i][t]* matrixB[t][j]


for k in matrixans:
    print(*k)