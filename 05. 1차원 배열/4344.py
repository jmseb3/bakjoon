c = int(input())

for test in range(c):
    n = list(map(int,input().split()))
    sum = 0
    cnt = 0
    for i in range(1,len(n)):
        sum += n[i]
    avg = sum/n[0]
    for i in range(1,len(n)):
        if n[i]>avg :
            cnt += 1
        else:
            next
    print("%.3f%%"%(cnt/n[0]*100))
