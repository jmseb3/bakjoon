def solution(n):
    data = list(str(n))

    answer = 0
    for x in data:
        answer += int(x)

    return answer
