t = input()
if t== " ":
    print(0)
else:
    cnt = 0
    for i in t.strip():
        if i == " ":
            cnt += 1
    print(cnt+1)
