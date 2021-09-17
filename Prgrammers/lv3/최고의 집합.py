def solution(n, s):
    q, r = divmod(s, n)
    if q == 0:
        return [-1]
    return[q for _ in range(n-r)] + [(q+1) for _ in range(r)]
