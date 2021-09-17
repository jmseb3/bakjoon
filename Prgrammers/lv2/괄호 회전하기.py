def solution(s):
    if s ==1:
        return 0
    answer =0
    def check(word):
        stack =[]
        for x in word:
            if x in ('[','(','{'):
                stack.append(x)
            else:
                if not stack:
                    return False
                y = stack.pop()
                if x==']' and y !='[':
                    return False
                if x=='}' and y !='{':
                    return False
                if x==')' and y !='(':
                    return False

        return True if not stack else False

    cnt = 0
    while True:
        if cnt == len(s)-1:
            break
    
        word = s[cnt:]+s[:cnt]
        if check(word):
            answer +=1
        cnt+=1

            
    return answer