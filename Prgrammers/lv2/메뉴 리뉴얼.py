from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    data =defaultdict(int)

    for order in orders:
        K = len(order)
        for i in range(1,K+1):
            c = list(combinations(order,i))
            for x in c:
                check =''.join(sorted(x))
                data[check] +=1
    answer =[]
    course_data = defaultdict(list)
    for k,v in data.items():
        if len(k) in course and v>=2:
            course_data[len(k)].append((v,k))
    for v in course_data.values():
        ck_max = max([x[0] for x in v])
        for x in v:
            if x[0]==ck_max:
                answer.append(x[1])
    answer.sort()
    print(answer)
    return answer