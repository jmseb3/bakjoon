def bunha(n):
    if n < 10:
        return n
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
check = []
for i in range(1,n):
    if bunha(i) == n :
        check.append(i)

if len(check) == 0:
    print(0)
else:
    print(check[0])
