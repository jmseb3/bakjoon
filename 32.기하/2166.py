N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.append(arr[0])
ans = 0

for i in range(N):
    ans += (arr[i][0]*arr[i+1][1])
    ans -= (arr[i][1]*arr[i+1][0])

print('%.1f'%(abs(ans)/2))
