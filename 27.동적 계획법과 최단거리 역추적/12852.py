import sys

input = sys.stdin.readline

N = int(input())


dp = [[0, []] for _ in range(N+1)]
dp[1]=[0,[1]]

def check(i,value):
    if i % value ==0 and dp[i//value][0] +1 <dp[i][0]:
        dp[i] = [dp[i//value][0]+1,dp[i//value][1] + [i]]

for i in range(2, N+1):
    dp[i]= [dp[i-1][0]+1,dp[i-1][1]+[i]]
    check(i,3)
    check(i,2)

print(dp[N][0])
for i in dp[N][1][::-1]:
    print(i,end=" ")