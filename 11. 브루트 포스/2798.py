n,m = map(int,input().split())
number = list(map(int,input().split()))

max = 0

for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            max_temp = number[i]+number[j]+number[k]
            if  max_temp > m:
                next
            else:
                if max <= max_temp:
                    max = max_temp

print(max)