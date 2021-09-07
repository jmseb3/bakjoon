def solution(n):
    data =list(str(n))
    data.sort(reverse=True)
    return int(''.join(data))

print(solution(118372))