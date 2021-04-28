n, m = map(int, input().split())
totalboard = []

for _ in range(n):
    totalboard.append(list(input()))

BW_checkboard = [[0 for _ in range(m)] for _ in range(n)]
WB_checkboard = [[0 for _ in range(m)] for _ in range(n)]


for i in range(m):
    for j in range(n):
        if (i+j) % 2==0:
            if totalboard[j][i] == "B":
                pass
            else:
                BW_checkboard[j][i] +=1
        else:
            if totalboard[j][i] =="W":
                pass
            else:
                BW_checkboard[j][i] +=1

for i in range(m):
    for j in range(n):
        if (i+j) % 2==0:
            if totalboard[j][i] == "W":
                pass
            else:
                WB_checkboard[j][i] +=1
        else:
            if totalboard[j][i] =="B":
                pass
            else:
                WB_checkboard[j][i] +=1

total = 64

for v in range(7, m):
    for w in range(7, n):
        sum = 0
        for p in range(8):
            for q in range(8):
                if BW_checkboard[w-q][v-p]:
                    sum += 1
        if sum <= total:
            total = sum

for v in range(7, m):
    for w in range(7, n):
        sum = 0
        for p in range(8):
            for q in range(8):
                if WB_checkboard[w-q][v-p]:
                    sum += 1
        if sum <= total:
            total = sum


print(total)
