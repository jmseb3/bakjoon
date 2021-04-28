n,k = map(int,input().split())
cost = [int(input()) for _ in range(n)]
dp =[0] * len(cost)

cost.sort(reverse=True)

def check(x,cost):
    cnt =0
    while True:
        if x >= cost:
            x= x-cost
            cnt+=1
        
        else:
            return x, cnt
    
    


for i in range(len(cost)):
    k, dp[i] = check(k, cost[i])

print(sum(dp))