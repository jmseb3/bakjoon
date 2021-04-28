n = int(input())
time = [list(map(int,input().split())) for _ in range(n)]

time.sort(key= lambda x:[x[1],x[0]])

cnt =0
start =0
for t in time:
    if t[0] >=start:
        start = t[1]
        cnt +=1

print(cnt)