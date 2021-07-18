import heapq as hq
import sys

input = sys.stdin.readline
n = int(input())
min_heap = []
max_heap =[]

while n > 0:
    x = int(input())
    if(len(max_heap)==len(min_heap)):
        hq.heappush(max_heap,(-x,x))
    else:
        hq.heappush(min_heap,(x,x))

    if (min_heap and min_heap[0][1] < max_heap[0][1]):
        temp1 = hq.heappop(max_heap)[1]
        temp2 = hq.heappop(min_heap)[1]
        hq.heappush(max_heap,(-temp2,temp2))
        hq.heappush(min_heap,(temp1,temp1))
    
    print(max_heap[0][1])
    n -= 1

