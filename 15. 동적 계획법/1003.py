t = int(input())

for i in range(t):
    n = int(input())
    count0 = [1,0]
    count1 = [0,1]
    for i in range(2,n+1):
        count0.append(count0[i-1]+count0[i-2])
        count1.append(count1[i-1]+count1[i-2])

    print("{} {}".format(count0[n],count1[n]))

