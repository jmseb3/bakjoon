n = int(input())
a = list(map(int,input().split()))
sum = 0

for i in a:
    sum += (i/max(a))*100

print(sum/len(a))