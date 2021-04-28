def facroial(x):
    number =1
    for j in range(1,x+1):
        number *= j
    return number
    
n,k = map(int,input().split())

print(facroial(n)//(facroial(k)*facroial(n-k)))
