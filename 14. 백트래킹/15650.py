n, m = map(int, input().split())
check = [False] * n
out = []


def recusive(index):
    if index == m:
        print(*out)
        return

    for i in range(n):
        if not check[i]:
            check[i] = True
            out.append(i+1)

            recusive(index+1)
            out.pop()

            for j in range(i+1, n):
                check[j] = False


recusive(0)

# 파이썬 모듈 사용시(조힙)
from itertools import combinations

n, m = map(int, input().split())

p = combinations(range(1,n+1),m)
for i in p:
    print(*i)