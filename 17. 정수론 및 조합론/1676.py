from math import factorial
n = factorial(int(input()))

cnt =0
while True :
    if n % 10 ==0:
        cnt +=1
        n //=10
    else:
        break
print(cnt)