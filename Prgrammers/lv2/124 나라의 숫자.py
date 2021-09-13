def solution(n):
    answer = ''
    while n:
        n,r =divmod(n,3)
        answer += '412'[r]
        if not r:
            n -=1
    
    return answer[::-1]
    


print(solution(3))
print(solution(6))
print(solution(9))
print(solution(12))