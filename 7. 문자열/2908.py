def chnum(n):
    ans = 0
    cnt = 100
    while True:
        if n >= 10:
            ans += (n % 10)*cnt
            n = n//10
            cnt = 10
        else:
            ans += n
            break
    return ans

a,b = map(int,input().split())

print(max(chnum(a),chnum(b)))