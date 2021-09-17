import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] *n
for i in range(1, n):
    for j in range(i):
        if(arr[i] > arr[j]):
            dp[i] = max(dp[i],dp[j]+1)

order = max(dp)
print(order)
ans =[]
for i in range(n-1,-1,-1):
    if dp[i] == order:
        ans.append(arr[i])
        order -=1

print(*ans[::-1])