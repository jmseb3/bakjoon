from itertools import combinations
def solution(numbers):
    c = combinations(numbers,2)
    answer = set()
    for x in c:
        answer.add(sum(x))
    return sorted(list(answer))