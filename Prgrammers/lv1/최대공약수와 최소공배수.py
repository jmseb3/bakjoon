# https://programmers.co.kr/learn/courses/30/lessons/12940
import math
def solution(n, m):
    ck =math.gcd(n,m)
    answer = [ck,n//ck*m]
    return answer