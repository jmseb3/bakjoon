def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    prev = -30001
    for r in routes:
        if r[0] > prev:
            prev = r[1]
            answer +=1
    return answer


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]	))
