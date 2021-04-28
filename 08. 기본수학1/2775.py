t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    num = list(range(1,n+1))
    
    for _ in range(k):
        for c in range(1,n):
            num[c] += num[c-1]

    print(num[n-1])