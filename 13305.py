import sys
input = sys.stdin.readline

n = int(input())
km = list(map(int, input().split()))
city = list(map(int, input().split()))

total = km[0]*city[0]
minvalue = city[0]

for i in range(1, n-1):
    minvalue = min(minvalue, city[i])
    total += minvalue*km[i]

print(total)
