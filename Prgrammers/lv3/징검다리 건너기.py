def solution(stones, k):
    answer = 0
    start, end = min(stones), max(stones)
    while start <= end:
        m = (start+end)//2
        n, max_jump = 1, 0
        for s in stones:
            if s-m >= 0:
                max_jump = max(n, max_jump)
                n = 1
            else:
                n += 1
        max_jump = max(n, max_jump)

        if max_jump >k:
            end = m-1

        else:
            start = m+1
            answer = max(answer,m)
            
    return answer
