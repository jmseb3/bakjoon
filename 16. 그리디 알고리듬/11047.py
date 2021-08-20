n, k = map(int, input().split())
cost = [int(input()) for _ in range(n)]
cost.sort(reverse=True)


cnt =0

for coin in cost:
    if k >=coin:
        cnt += k//coin
        k = k%coin
    
    if k ==0:
        break

print(cnt)
