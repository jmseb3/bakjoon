import sys
input = sys.stdin.readline
stack =[0]
for _ in range(int(input())):
    n = int(input())
    if n ==0:
        stack.pop(-1)
    else:
        stack.append(n)

print(sum(stack))


