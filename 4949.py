check =['(',')','[',']']

def isps(ps):
    stack =[]

    for i in range(len(ps)):
        stack.append(ps[i])

        if ps[i] == ')':
            if len(stack) >= 2:
                if stack[-2] =='(':
                    stack.pop()
                    stack.pop()
                else:
                    return False
            else:
                return False
        elif ps[i] == ']':
            if len(stack) >= 2:
                if stack[-2] =='[':
                    stack.pop()
                    stack.pop()
                else:
                    return False
            else:
                return False
    
    if stack:
        return False
    else:
        return True

while True:
    s = input()
    if s ==".":
        break
    stack_temp=[]
    s = list(s.lower())

    for k in s:
        if k in check:
            stack_temp.append(k)
            
    if isps(stack_temp):
        print("yes")
    else:
        print("no")
