a = int(input())
b = int(input())
c = int(input())

sum = a* b* c
a= []
b= [0,0,0,0,0,0,0,0,0,0]
cnt = 0
while True:
    a.append(sum%10)
    b[a[cnt]] += 1
    cnt +=1
    if sum >= 10:
        sum = sum//10
    else:
        break

for i in range(10):
    print(b[i])