def check(n):
    if n < 2:
        return False
    elif n ==2:
        return True
    for k in range(2, int(n**(0.5))+1):
        if n % k == 0:
            return False
    return True

primelist = list(range(0,20001))
for i in range(len(primelist)):
    primelist[i] = check(i)
prime=[]
for v, k in enumerate(primelist):
    if k:
        prime.append(v)

for _ in range(int(input())):
    n = int(input())
    for j in range(int(n/2),1,-1):
        if j in prime:
            if n-j in prime:
                print(j, n-j)
                break