def solution(s):
    answer =0
    stack =[]

    if len(s) <2:
        return 0

    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1] ==i:
            stack.pop()
        elif stack[-1] != i:
            stack.append(i)
    
    
    return 0 if stack else 1
print(solution("baabaa"))
print(solution("cdcd"))