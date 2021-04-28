import sys

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    x, y = map(int, input().split())
    arr.append((x,y))

arr.sort()

def length_square(a, b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2


def check(start, end):
    # 거리계산불가능
    if start == end:
        return float('inf')
    else:
        mid = (start+end)//2
        min_length = min(check(start, mid), check(mid+1, end))
        target = []

        for i in range(mid, start-1, -1):
            if(arr[i][0]-arr[mid][0]) ** 2 < min_length:
                target.append(arr[i])
            else:
                break

        for j in range(mid+1, end+1):
            if (arr[j][0]-arr[mid][0]) ** 2 < min_length:
                target.append(arr[j])
            else:
                break

        target.sort(key=lambda x: x[1])
        for i in range(len(target)-1):
            for j in range(i+1,len(target)):
                if (target[i][1]-target[j][1])**2<min_length:
                    min_length = min(min_length,length_square(target[i],target[j]))
                else:
                    break
        return(min_length)


if len(arr) != len(set(arr)):
    print(0)
else:
    print(check(0,len(arr)-1))
    
