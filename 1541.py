n =input().split('-')

for i in range(len(n)):
    if "+" in n[i]:
        x= n[i].split('+')
        temp = 0
        for k in x:
            temp += int(k)
        n[i] =temp
    else:
        n[i] = int(n[i])
  
ans = n[0] -sum(n[1:len(n)+1])
print(ans)