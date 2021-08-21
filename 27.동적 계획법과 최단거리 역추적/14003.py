import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
arr = [0]+list(map(int, input().split()))
dp = [0] *(N+1)

cmp = [-1000000001] # 이진탐색을 위해 생성.
maxVal = 0 #최대값을 저장할 변수
for i in range(1, N+1):
    if cmp[-1] < arr[i]: #이진탐색으로 저장된 값들은 정렬되므로 맨 뒤의 값 비교.
        cmp.append(arr[i])
        dp[i] = len(cmp) - 1
        maxVal = dp[i]
    else:
        dp[i] = bisect_left(cmp, arr[i]) #현재 값이 어느 위치의 값에 해당하는지 비교.
        cmp[dp[i]] = arr[i] #cmp 업데이트.

print(maxVal) #최대 길이 출력
res =[]
for i in range(N,0,-1):
    if dp[i] == maxVal:
        res.append(arr[i])
        maxVal-=1
res.reverse()
print(*res)