n = int(input())
time = list(map(int,input().split()))
dp =[0] * n
time.sort()
for i in range(n):
    dp[i] = sum(time[0:i+1])

print(sum(dp))