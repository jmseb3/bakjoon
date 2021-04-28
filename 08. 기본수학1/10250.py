t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    if n%h ==0:
        cnt = n/h
        dong = h
        ho = int(cnt)
    else:
        cnt =n//h
        dong = n-h*cnt
        ho = cnt+1

    if ho < 10:
        print(str(dong)+"0"+str(ho))
    else:
        print(str(dong)+str(ho))