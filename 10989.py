import sys
n = int(input())
check = [0] *100001

for _ in range(n):
    num = int(sys.stdin.readline())
    check[num] +=1

for v,k in enumerate(check):
    if k !=0 :
        for _ in range(k):
            print(v)