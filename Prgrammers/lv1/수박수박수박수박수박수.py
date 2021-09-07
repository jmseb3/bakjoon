def solution(n):
    data = '수박' *(n//2)
    return data if n%2==0 else data+'수'