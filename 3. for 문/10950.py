t = int(input())
c=[]
for i in range(t):
    a,b = map(int,input().split())
    c.append(a+b)

for i in range(t):
    print(c[i])