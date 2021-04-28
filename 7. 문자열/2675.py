t = int(input())
ans = ""
for _ in range(t):
    r, s = map(str, input().split())
    for i in s:
        ans += i * int(r)
    
    print(ans)
    ans=""
