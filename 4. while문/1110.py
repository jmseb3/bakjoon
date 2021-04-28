n = int(input())
num = n
cnt = 0
while True :
    if n < 10:
        n= n*10 +n
        cnt +=1
    else:
        n_temp = (n//10) + (n%10)
        n = (n%10)*10+ (n_temp%10)
        cnt +=1

    if n == num:
        print(cnt)
        break