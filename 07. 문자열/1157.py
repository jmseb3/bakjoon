t = list(input().upper())
alpha_list = {}
for i in range(65, 91):
    alpha_list[chr(i)] = 0

for i in t:
    alpha_list[i] += 1

cnt = 0
for v, k in alpha_list.items():
    if k == max(alpha_list.values()):
        cnt += 1
        ans = v


if cnt == 1:
    print(ans)
else:
    print("?")
