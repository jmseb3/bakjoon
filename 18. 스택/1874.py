import sys
input = sys.stdin.readline

n = int(input())
cnt =1
stack =[]
result =[]
temp = True
for i in range(n):
    x = int(input())

    while cnt <= x:
        stack.append(cnt)
        result.append('+')
        cnt +=1

    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        temp = False
        

if temp:
    for k in result : print(k)
else:
    print("NO")
        
