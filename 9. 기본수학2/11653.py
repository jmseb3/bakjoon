import sys

n = int(sys.stdin.readline())

if n == 1:
    pass
else:
    i = 2
    while True:
        if n / i == 1:
            print(i)
            break
        if n % i == 0:
            print(i)
            n = n/i
        else:
            i += 1