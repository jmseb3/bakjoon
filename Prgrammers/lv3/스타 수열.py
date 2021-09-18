from collections import defaultdict
def solution(a):
    dic = defaultdict(list)
    for i, v in enumerate(a):
        dic[v].append(i)
        
    l = len(a)
    answer = 0
    for k, v in dic.items():
        if len(v) <= answer // 2:
            continue
        else:
            now = a.copy()
            cnt = 0
            for j in v:
                if j > 0 and now[j-1] != k:
                    now[j-1] = k
                    cnt += 2
                elif j < l-1 and now[j+1] != k:
                    now[j+1] = k
                    cnt += 2
            answer = max(answer, cnt)
    return answer
