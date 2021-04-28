import sys

input = sys.stdin.readline

n = int(input())
data_n = set(map(int, input().split()))

m = int(input())
data_m = list(map(int, input().split()))

for i in data_m:
    if i in data_n:
        print(1)
    else:
        print(0)