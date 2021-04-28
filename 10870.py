fibo =[0,1]
n = int(input())

if n<=1:
    print(fibo[n])
else:
    for i in range(n-1):
        fibo.append(fibo[i]+fibo[i+1])
    print(fibo[n])