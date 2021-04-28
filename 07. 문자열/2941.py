a = input()

cnt = 0
i = 0
wordlist = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]
while True:
    if a[i:i+2] in wordlist:
        cnt += 1
        i += 2
    elif a[i:i+3] == "dz=":
        cnt += 1
        i += 3
    else:
        cnt += 1
        i += 1

    if i == len(a):
        break

print(cnt)