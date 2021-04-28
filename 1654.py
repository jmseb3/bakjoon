import sys

input = sys.stdin.readline

k, n = map(int, input().split())

data = [int(input()) for _ in range(k)]

start =1
end = max(data)

while start <= end:
    mid = (start+end)//2
    cnt =0
    for i in data:
        cnt += i//mid
    
    if cnt >=n:
        start = mid +1
        ans = mid
    else:
        end = mid -1

print(ans)

