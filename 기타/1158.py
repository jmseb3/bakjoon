N, K = map(int, input().split())
arr =[i for i in range(1,N+1)]
ans =[]
num = K-1

for i in range(N):
    if (len(arr)<=num):
        num %= len(arr)


    ans.append(str(arr.pop(num)))
    num +=K-1

print("<",', '.join(ans),">",sep="")