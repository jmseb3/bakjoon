n=int(input())
Sum=1
for i in range(0,n):
    Sum+=6*i 
    if Sum>=n:
        print(i+1)
        break 