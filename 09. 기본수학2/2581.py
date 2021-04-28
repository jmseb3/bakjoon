m = int(input())
n = int(input())
number = []
for k in range(m,n+1):
    if k == 1:
        next
    check = 0
    for i in range(2, k):
        if k % i != 0:
            check += 1
        else:
            break
    if check + 2 == k:
        number.append(k)

if number != [] :
    print(sum(number))
    print(min(number))
else:
    print("-1")
