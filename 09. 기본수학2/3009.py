x = [0,0,0]
y = [0,0,0]
ans = [0,0]
for i in range(3):
    x[i], y[i] = map(int, input().split())

for i in range(3):
    if x[i%3] == x[(i+1) %3]:
        ans[0] = x[(i+2)%3]

    if y[i%3] == y[(i+1)%3]:
        ans[1] = y[(i+2)%3]
    
print(ans[0],ans[1])