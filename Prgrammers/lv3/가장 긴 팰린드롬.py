def solution(s):
    def check(a, b):
        temp = s[a:b+1]
        return temp == temp[::-1]
    answer = 0
    start = 0
    N = len(s)
    while start < N:
        ck = s[start]
        for idx in range(start, N):
            if s[idx] == ck:
                if check(start,idx):
                    answer = max(answer,idx-start+1)
        start+=1
    return answer
