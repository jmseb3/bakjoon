import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
ans = abs(N-100)

if M == 0:
    ans = min(ans, len(str(N)))
else:
    broken = list(input().rstrip().split())
    for i in range(1000001):
        flag = True
        str_i = str(i)
        for j in str_i:
            if j in broken:
                flag = False
                break
        if flag:
            ans = min(ans, abs(i-N)+len(str_i))
print(ans)
