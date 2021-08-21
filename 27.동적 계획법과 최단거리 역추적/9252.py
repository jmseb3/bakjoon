import sys
input = sys.stdin.readline

alpha1,alpha2 = input().rstrip(),input().rstrip()
len1,len2  = len(alpha1),len(alpha2)

dp = [[[0,[]]] * (len1+1) for _ in range(len2+1)]
for i in range(1,len2+1):
    for j in range(1,len1+1):
        if alpha2[i-1] == alpha1[j-1]:
            dp[i][j] = [dp[i-1][j-1][0]+1,dp[i-1][j-1][1] + [alpha2[i-1]]]
        else:
            if dp[i-1][j][0] >= dp[i][j-1][0]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

cnt, ans = dp[len2][len1]
print(cnt)
print("".join(ans))

