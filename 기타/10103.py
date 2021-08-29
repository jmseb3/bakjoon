import sys
input = sys.stdin.readline
data = [100, 100]
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())

    if a > b:
        data[1] -= a
    elif b > a:
        data[0] -= b
    else:
        continue

for xx in data:
    print(xx)
