import math
def solution(n):
    k = int(math.sqrt(n))
    if k**2 == n:
        return(k+1)**2
    else:
        return -1
