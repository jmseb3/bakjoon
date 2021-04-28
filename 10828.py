import sys
input = sys.stdin.readline

n = int(input())
stack =[]
for _ in range(n):
    order = list(map(str, input().rstrip().split()))
    if order[0] =="push":
        stack.append(order[1])
    elif order[0] =="pop":
        if len(stack) ==0 :
            print(-1)
        else:
            print(stack.pop(-1))
    elif order[0] =='size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack) ==0:
            print(1)
        else:
            print(0)
    elif order[0] =='top':
        if len(stack) ==0 :
            print(-1)
        else:
            print(stack[-1])

