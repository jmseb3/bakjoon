from itertools import product

def solution(word):
    a=[''.join(list(j)) for i in range(1,6) for j in product(['A','E','I','O','U'],repeat=i)]
    a.sort()
    return a.index(word)+1
