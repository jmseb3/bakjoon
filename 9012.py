import sys
input = sys.stdin.readline

def isps(ps):
    stack =[]
    ps = list(ps)
    ps.pop(-1)

    for i in range(len(ps)):
        stack.append(ps[i])

        if ps[i] == ')':
            if len(stack) >= 2:
                stack.pop()
                stack.pop()
            else:
                return "NO"
    
    if stack:
        return "NO"
    else:
        return "YES"

for _ in range(int(input())):
    ps = input()
    print(isps(ps))


