def solution(lottos, win_nums):
    rank =[6,6,5,4,3,2,1]
    zero = lottos.count(0)
    ans =0
    for x in win_nums:
        if x in lottos:
            ans+=1
    
    return [rank[zero+ans],rank[ans]]