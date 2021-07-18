import heapq as hq
import sys

input = sys.stdin.readline

n = int(input())
heap = []

while n > 0:
    x = int(input())

    if (x == 0):
        try:
            print(hq.heappop(heap)[1])
        except IndexError:
            print(0)
    else:
        if(x < 0):
            hq.heappush(heap, (-x, x))
        else:
            hq.heappush(heap, (x, x))

    n -= 1
