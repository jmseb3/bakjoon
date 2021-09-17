def solution(arr):
    if len(arr)==1:
        return [-1]
    
    ck = min(arr)
    arr.remove(ck)
    return arr