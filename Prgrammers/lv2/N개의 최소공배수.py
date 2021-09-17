from math import gcd
def solution(arr):
    answer = arr[0]
    for idx in range(1,len(arr)):
        answer = answer *arr[idx]//gcd(answer,arr[idx])

    return answer