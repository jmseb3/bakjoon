def bunha(n):
    if(n < 10):
        return 2*n
    sum = n
    while True:
        if n >= 10:
            sum += (n % 10)
            n = int(n//10)
        else:
            sum += n
            break
    return sum


n = int(input())
ans = 0
for i in range(1, n+1):
    if(bunha(i) == n):
        ans = i
        break
print(ans)
