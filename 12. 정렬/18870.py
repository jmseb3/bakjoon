import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = [0 for _ in range(n)]

for i in range(n):
    cnt = 0
    for j in range(n):
        if(arr[i]>arr[j]):
            cnt +=1
    ans[i] = cnt

print(*ans)
