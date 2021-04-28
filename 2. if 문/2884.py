h,m = map(int,input().split())


if h==0:
    if m >= 45:
        m= m-45
        print(h,m)
    else:
        h= 23
        m = 60 +(m-45)
        print(h, m)
else:
    if m >= 45:
        m= m-45
        print(h,m)
    else:
        h = h-1
        m = 60 +(m-45)
        print(h, m)