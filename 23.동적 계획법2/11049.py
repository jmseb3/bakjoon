n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

def solution(n,arr):
    if n==1:
        return 0
    if n==2:
        return arr[0][0] * arr[0][1] * arr[1][1]
        
    dp =[[0 for _ in range(n)] for _ in range(n)]
  
    for i in range(1,n):
        for j in range(n-i):
            if i==1:
                dp[j][j+1] = arr[j][0]*arr[j][1]*arr[j+1][1]
                continue
            
            dp[j][j+i] = 2**32
            for k in range(j,j+i):
                dp[j][j+i] = min(dp[j][j+i],dp[j][k]+dp[k+1][j+i]+arr[j][0]*arr[k][1]*arr[j+i][1])


    return dp[0][n-1]

print(solution(n,arr))