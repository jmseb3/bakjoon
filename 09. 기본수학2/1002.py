from math import sqrt
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    X = x2 - x1
    Y = y2 - y1
    xy_range = sqrt(X**2+Y**2)
    if xy_range==0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if (r1+r2 ==xy_range) or (abs(r2-r1)==xy_range):
            print(1)
        elif (r1+r2) > xy_range and (abs(r2-r1))<xy_range:
            print(2)
        else:
            print(0)