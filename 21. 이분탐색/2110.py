import sys

input = sys.stdin.readline

n, c = map(int, input().split())
data = [int(input()) for _ in range(n)]

data.sort()
start = 0
end = max(data)-min(data)

while start <= end:
    mid = (start+end)//2

    cnt = 1
    base = data[0]
    for i in range(1, n):
        if data[i] - base >= mid:
            cnt += 1
            base = data[i]

    if cnt >= c:
        start = mid+1
        ans = mid
    else:
        end = mid - 1

print(ans)
