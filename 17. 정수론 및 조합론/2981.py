def gcd(x, y):
    while y != 0:
        k = x % y
        x, y = y, k

    return x

n = int(input())
number = [int(input()) for _ in range(n)]
number.sort()
g = abs(number[1] - number[0])

for i in range(1, n-1):
    g = gcd(g, abs(number[i+1] - number[i]))

result = []
for i in range(2, int(g**0.5)+1):
    if g % i == 0:
        result.append(i)
        result.append(g // i)

result.append(g)

result = list(set(result))

result.sort()

print(*result)