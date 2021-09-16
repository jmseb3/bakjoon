def solution(n, money):
    M =len(money)
    MOD = 1000000007
    table = [[0 for _ in range(n+1)] for _ in range(M)]
    table[0][0] = 1

    for i in range(money[0],n+1,money[0]):
        table[0][i] = 1

    for y in range(1,M):
        for x in range(n+1):
            if x >=money[y]:
                table[y][x] = (table[y-1][x] + table[y][x-money[y]]) %MOD
            else:
                table[y][x] = table[y-1][x]
    return table[-1][-1]
