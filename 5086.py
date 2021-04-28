while True:
    x,y = map(int,input().split())
    if x + y ==0 :
        break

    if x/y > 1:
        if x % y ==0:
            print('multiple')
        else:
            print('neither')
    else:
        if y % x ==0 :
            print('factor')
        else:
            print('neither')
    