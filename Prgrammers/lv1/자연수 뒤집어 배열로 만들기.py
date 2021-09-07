def solution(n):
    answer = []
    while True:
        if n<10:
            answer.append(n)
            break
        else:
            answer.append(n%10)
            n //=10
    
    return answer