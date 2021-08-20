import sys
input = sys.stdin.readline

N, C = map(int, input().split())
weights = list(map(int, input().split()))
aw, bw = weights[:N//2], weights[N//2:]
asum, bsum = [], []


def bruteforce(warr, sumarr, l, w):
    if l >= len(warr):
        sumarr.append(w)
        return
    bruteforce(warr, sumarr, l+1, w)
    bruteforce(warr, sumarr, l+1, w+warr[l])


def binarysearch(arr, target, start, end):
    while start < end:
        mid = (start+end)//2
        if arr[mid] <= target:
            start = mid+1
        else:
            end = mid
    return end


bruteforce(aw, asum, 0, 0)
bruteforce(bw, bsum, 0, 0)
bsum.sort()
print(asum)
print(bsum)
cnt = 0
for i in asum:
    if C-i < 0:
        continue
    cnt += binarysearch(bsum, C-i, 0, len(bsum))
print(cnt)
