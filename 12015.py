import sys

input = sys.stdin.readline

def checkis(a:list):
    if (a == a.sort):
        return True
    else:
        return False

n =int(input)
arr = list(map(int,input().split()))

start = 0
end = n
while start <= end:
    mid = (start+end)//2

    temp = 0
    for i in range(1, n+1):
        temp += min(mid//i, n)
    if temp >= k:
        ans = mid
        end = mid-1
    else:
        start=mid + 1

print(ans)