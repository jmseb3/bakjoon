from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q= deque(maxlen=cacheSize)
    if cacheSize==0:
        return len(cities)*5
    for c in cities:
        c = c.lower()
        if c not in q:
            q.append(c)
            answer+=5
        else:
            q.remove(c)
            q.append(c)
            answer+=1
            
    return answer