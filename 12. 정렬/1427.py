n = int(input())

list = []

while True:
    if n >= 10:
        list.append(n%10)
        n = n//10
    else:
        list.append(n)
        break

list.sort(reverse=True)

ans =""
for j in list:
    ans += str(j)

print(ans)