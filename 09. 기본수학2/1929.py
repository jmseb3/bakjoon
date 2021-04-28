import sys

def check(n):
    check = 2
    for k in range(2,int(n**(0.5)+1)):
        if n % k == 0:
            return False
    return print(i)

m, n = map(int, sys.stdin.readline().split())
if m == 1:
    m += 1

for i in range(m, n+1):
    check(i)