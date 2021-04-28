import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
stack =[]
result =[-1]*n
for index, num in enumerate(A):

    while stack and A[stack[-1]] < num:
        result[stack[-1]] = num
        stack.pop()

    stack.append(index)

print(*result)