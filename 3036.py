def gcd(x, y):
    while y != 0:
        k = x % y
        x, y = y, k

    return x


n = int(input())
ring = list(map(int,input().split()))
number = ring[0]
for k in range(1,n):
    n = gcd(ring[k],number)
    print("{}/{}".format(number//n,ring[k]//n))
