import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

start =0
end = max(data)

while start <= end:
    mid = (start+end)//2
    print("----",start,mid,end)
    cnt =0
    for i in data:
        if i>=mid:
            cnt += (i -mid)

    print("----",cnt)
    
    if cnt >=m:
        start = mid +1
        ans = mid
    else:
        end = mid -1

    print("--------------------------------")
    

print(ans)

