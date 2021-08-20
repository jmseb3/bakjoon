import sys
input = sys.stdin.readline

N, S = map(int, input().split())

arr = list(map(int, input().split()))
sum_arr = [0 for _ in range(N)]
sum_arr[0] = arr[0]

for idx in range(1, N):
    sum_arr[idx] = sum_arr[idx-1] + arr[idx]
start, end = 0, 0
ans = int(1e9)

while start <= end:

    if end == N:
        break

    ck = sum_arr[end]-sum_arr[start-1] if start != 0 else sum_arr[end]

    if ck >= S:
        ans = min(ans, end-start+1)
        start += 1
    else:
        end += 1

print(0 if ans == int(1e9) else ans)
