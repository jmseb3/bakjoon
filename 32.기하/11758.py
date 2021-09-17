arr = []

for _ in range(3):
    arr.append((list(map(int,input().split()))))
arr.append(arr[0])
ans = 0
for i in range(3):
    ans += (arr[i][0]*arr[i+1][1])
    ans -= (arr[i][1]*arr[i+1][0])


if ans > 0:
    print(1)
elif ans == 0:
    print(0)
else:
    print(-1)
