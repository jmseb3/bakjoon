def solution(d, budget):
    answer = 0
    d.sort()
    for x in d:
        if budget- x>=0:
            answer +=1
            budget -=x
        else:
            break
    return answer