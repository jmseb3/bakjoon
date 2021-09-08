def solution(left, right):
    answer = 0
    for number in range(left, right+1):
        if int(number**0.5)**2 == number:
            answer -= number
        else:
            answer += number

    return answer
