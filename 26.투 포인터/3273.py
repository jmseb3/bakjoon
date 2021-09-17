import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
X = int(input())
start, end = 0, N-1
cnt =0

while start!=end:
    ck = arr[start] +arr[end]
    if ck ==X:
        cnt +=1
        start +=1
    elif ck >X:
        end -=1
    else:
        start+=1

print(cnt)
    
