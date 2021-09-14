import heapq


def solution(n, works):
    if n >= sum(works):
        return 0
    heap = []
    for x in works:
        heapq.heappush(heap, (-x, x))
    
    while n:
        n -= 1
        now = heapq.heappop(heap)[1] -1
        if now ==0:
            continue
        heapq.heappush(heap, (-now, now))
        
    return sum(list(x[1]**2 for x in heap))
