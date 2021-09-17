def solution(n, t, m, p):
    answer = ''
    data = ''
    num = 0
    while len(data) < t*m:
        data +=ch_jin(num, n)
        num+=1
    for idx in range(p-1,t*m,m):
        answer +=data[idx]
    return answer

def ch_jin(num,base):
    T ="0123456789ABCDEF"
    q,r =divmod(num,base)
    if q==0:
        return T[r]
    else:
        return ch_jin(q,base) +T[r]
