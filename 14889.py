from itertools import combinations

n = int(input())
power = [list(map(int, input().split())) for _ in range(n)]


p = combinations(range(1, n+1), n//2)

ablelist = []
for i in p:
    ablelist.append(list(i))

cnt = len(ablelist)//2


def ans():
    powercount = []

    for j in range(cnt):
        powercount.append(
            abs(check_sum(ablelist[j])-check_sum(ablelist[2*cnt-j-1])))

    return min(powercount)


def check_sum(numberlist):
    sum = 0
    for j in numberlist:
        for k in numberlist:
            sum += power[j-1][k-1]

    return sum


print(ans())
