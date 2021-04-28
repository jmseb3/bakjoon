t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    distance = y-x
    cnt = 0
    k = 1
    total = 0
    while total < distance:
        cnt += 1
        total += k
        if cnt % 2 == 0:
            k += 1

    print(cnt)