import sys
input = sys.stdin.readline

min_value = 2*(10**9)

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
start =0
end = N-1

while start!=end:
    ck = arr[start]+arr[end]
    if abs(ck) <abs(min_value):
        ans = [arr[start],arr[end]]
        min_value =ck
        if ck ==0:
            break

    if ck<0:
        start +=1
    else:
        end -=1

print(*ans)
