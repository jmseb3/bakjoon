import sys
import bisect
from itertools import combinations
input = sys.stdin.readline

N, C = map(int, input().split())
weights = list(map(int, input().split()))
aw, bw = weights[:N//2], weights[N//2:]


def sum_list(arr):
    sum_arr = []
    for i in range(len(arr)+1):
        sum_arr += list(map(sum, combinations(arr, i)))
    return sum_arr


asum, bsum = sum_list(aw), sum_list(bw)
asum.sort()

cnt = 0
for b in bsum:
    cnt += bisect.bisect_right(asum, C-b)

print(cnt)
