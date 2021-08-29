T = int(input())

for _ in range(T):
    data = list(map(int,input().split()))
    data.sort()
    if (data[-2]-data[1])>=4:
        print("KIN")
    else:
        print(sum(data[1:-1]))