n = int(input())
number = list(map(int, input().split()))
cnt = 0
for k in number:
    if k == 1:
        next
    check = 0
    for i in range(2, k):
        if k % i != 0:
            check += 1
    if check + 2 == k:
        cnt += 1

print(cnt)