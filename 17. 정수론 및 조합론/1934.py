for _ in range(int(input())):
    x,y = map(int,input().split())
    minnum =min(x,y)
    n =0
    for i in range(1,minnum+1):
        if x%i ==0 and y %i ==0 :
            n =i
    print(int(x*y/n))