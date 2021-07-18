import sys

input = sys.stdin.readline

t = int(input())

while t >0:

    k = int(input())
    time_arr = list(map(int,input().split()))
    dp = [ 0 for _ in range(k-1)]

    for idx in range(k-1):
        time_arr.sort()
        temp = time_arr[0]+time_arr[1]
        dp[idx] = temp
        time_arr[0:2] = [temp]
    
    print(dp)
    print(sum(dp))

    t -=1