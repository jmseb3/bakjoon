from itertools import combinations

def solution(nums: list):
    nums.sort()
    N= sum(nums[-3:])
    answer = 0
    
    data = [False, False]+[True] * (N-1)
    for idx in range(2, N+1):
        if data[idx]:
            for j in range(2*idx,N+1,idx):
                data[j] = False
                
    for x in combinations(nums,3):
        if data[sum(x)]:
            answer +=1

    return answer
