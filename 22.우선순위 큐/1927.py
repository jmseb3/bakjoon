import heapq as hq
import sys

input = sys.stdin.readline
n =int(input())
heap = []
while n>0:
    x= int(input())
    if(x==0):
        try:
            print(hq.heappop(heap))
        except IndexError:
            print(0)
    else:
        hq.heappush(heap,x)
    n-=1

