def solution(n):
    data = [False, False]+[True] * (n-1)
    answer = 0

    for idx in range(2, n+1):
        if data[idx]:
            answer +=1
            for j in range(2*idx,n+1,idx):
                data[j] = False
        
    
    return answer
