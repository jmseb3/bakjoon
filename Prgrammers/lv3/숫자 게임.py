import heapq


def solution(A, B):
    heapq.heapify(A)
    heapq.heapify(B)
    answer = 0
    while B:
        a = heapq.heappop(A)
        b = heapq.heappop(B)
        if a < b:
            answer += 1
        else:
            heapq.heappush(A, a)

    return answer
