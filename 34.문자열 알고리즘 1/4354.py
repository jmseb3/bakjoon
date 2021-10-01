while True:
    s = input()
    if s == ".":
        break
    elif s =="":
        print(0)
    else:
        for length in range(len(s),0,-1):
            cnt,ck =divmod(len(s),length)
            if ck != 0:
                continue
            temp = s[:cnt]
            if (temp)*length == s:
                print(length)
                break
