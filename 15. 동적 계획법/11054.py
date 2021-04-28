n = int(input())
arr = list(map(int, input().split()))
dp = [0] *n
dp1 = [1] * n
dp2 = [1] * n

for i in range(1,n):
    for j in range(i):
        if arr[j] <arr[i]:
            dp1[i] = max(dp1[i],dp1[j]+1)

arr = arr[::-1]
for i in range(1,n):
    for j in range(i):
        if arr[j] <arr[i]:
            dp2[i] = max(dp2[i],dp2[j]+1)

dp2 =dp2[::-1]

for j in range(n):
    dp[j] =dp1[j]+dp2[j]

print(max(dp)-1)