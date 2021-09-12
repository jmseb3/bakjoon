def solution(n, a, b):
    answer = 1
    if a > b:
        a, b = b, a

    while True:
        if b % 2 == 0 and b == a+1:
            break

        aq, ar = divmod(a, 2)
        bq, br = divmod(b, 2)
        if ar == 0:
            a = aq
        else:
            a = aq+1

        if br == 0:
            b = bq
        else:
            b = bq+1
        answer +=1

    return answer
