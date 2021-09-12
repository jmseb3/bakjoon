from itertools import permutations
from copy import deepcopy
from bisect import bisect_left
def solution(expression):
    buho = ['-','*','+']
    data =[]
    temp =''
    for s in expression:
        if s in buho:
            data.append(int(temp))
            data.append(s)
            temp=""
        else:
            temp +=s
    data.append(int(temp))
    print(data)
    answer = 0

    for qry in permutations(buho):
        temp = deepcopy(data)
        for st in qry:
            while True:
                if st not in temp:
                    break
                ck = temp.index(st)
                print(ck)
                print(cal_num(temp[ck-1],temp[ck+1],st))
                temp[ck-1:ck+2] = [cal_num(temp[ck-1],temp[ck+1],st)]
                print(temp)
        answer = max(answer,abs(temp[0]))
    return answer

def cal_num(x,y,type):
    if type=='-':
        return x-y
    if type =='*':
        return x*y
    if type =='+':
        return x+y

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))