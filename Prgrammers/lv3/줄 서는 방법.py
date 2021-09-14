import math


def solution(n, k):
    person = list(range(1, n+1))
    answer = []
    while person:
        temp = math.factorial(n-1)
        q, r = divmod(k, temp)
        q = q-1 if r == 0 else q
        answer.append(person.pop(q))
        n -= 1
        k = r

    return answer


print(solution(3, 5))
