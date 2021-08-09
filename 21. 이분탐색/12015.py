import sys
input = sys.stdin.readline


def checkis(a: list):
    if (a == a.sort):
        return True
    else:
        return False


n = int(input())
arr = list(map(int, input().split()))
dp = [0]

for i in range(n):
    low = 0
    high = len(dp)-1
    while low <= high:
        mid = (low+high)//2
        if dp[mid] < arr[i]:
            low = mid+1
        else:
            high = mid-1
    if low >= len(dp):
        dp.append(arr[i])
    else:
        dp[low] = arr[i]
    print(dp)

print(len(dp)-1)
