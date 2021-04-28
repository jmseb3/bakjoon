import sys

def check(n):
    if n < 2:
        return False
    elif n ==2:
        return True

    for k in range(2, int(n**(0.5))+1):
        if n % k == 0:
            return False
    return True


primelist = list(range(0,250000))
for i in range(len(primelist)):
    primelist[i] = check(i)

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    cnt =0
    for j in range(n+1,2*n+1):
        if primelist[j]:
            cnt +=1
    print(cnt)
