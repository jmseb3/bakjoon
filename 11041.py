import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
p = 1000000007


# 페르마소정리 이용
# p가 소수이고 a,p가 서로수 일때 a**(p-1)%p = 1
# 변형을 시켜서 a**(p-2)%p = p**(-1) 으로 사용가능하다.
# 여기서 주어진수 p=1000000007 은 소수이다.

# a^m에 대하여 
# 짝수면 m//2
# 홀수면 m//2 한뒤 a를 곱해줌


def pow(n, k):
    global p
    if k == 1:
        return n

    next_pow = pow(n, k//2)

    if k % 2 == 0:
        return (next_pow**2) % p
    else:
        return ((next_pow ** 2) * n) % p


factori = [1] * (n+1)

for i in range(2, n+1):
    factori[i] = (factori[i-1]*i) % p


print(factori[n]*(pow(factori[n-k], p-2))*(pow(factori[k], p-2)) % p)
