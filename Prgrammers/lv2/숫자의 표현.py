def solution(n):
    answer = 1
    for ck in range(n//2+1,-1,-1):
        num = ck
        ans = ck
        while True:
            if ans >=n:
                if ans ==n:
                    answer +=1
                break
               

            num -=1
            if num<1:
                break
            ans += num
        
    return answer

print(solution(15))