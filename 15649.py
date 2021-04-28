n, m = map(int, input().split())
check = [False] * n
out = []

def recusive(index):
    if index == m:
        print(*out)
        return
        
    for i in range(n):

        if not check[i]:
            check[i] =True
            out.append(i+1)

            recusive(index+1)

            check[i]= False
            out.pop()

recusive(0)

# 파이썬 모듈 사용시(순열)
from itertools import permutations

n, m = map(int, input().split())

p = permutations(range(1,n+1),m)
for i in p:
    print(*i)