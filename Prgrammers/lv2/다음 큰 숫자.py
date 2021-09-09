def solution(n):
    cnt= bin(n)[2:].count('1')
    ck =n+1
    while True:
        if bin(ck)[2:].count('1') == cnt:
            return ck
        
        ck+=1

print(solution(78))